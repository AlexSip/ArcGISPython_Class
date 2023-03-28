import arcpy
import csv
import os
import tempfile
import glob
import shutil

# Set overwriteOutput to True to allow overwriting of output files, this can also prevent errors
arcpy.env.overwriteOutput = True

# Create a temporary directory using the tempfile module
temp_dir = tempfile.mkdtemp()

# Set the workspace to a temporary directory
arcpy.env.workspace = temp_dir

# This will read the combined data set sheet
data = []  # Create an empty list to store data
combined_data_path = "Fish_data.csv"
with open(combined_data_path) as combinedData_csv:
    csv_reader = csv.reader(combinedData_csv, delimiter=',')   # Create a csv_reader object
    line_count = 0   # Declare a variable to keep track of the number of lines read from the file
    # Loop through each row in the csv_reader
    for row in csv_reader:
        if line_count != 0:  # Skip the first row (because of the headers)
            if row[0] not in data:  # Checks if the data value in the first column of the row is not already in the data list
                data.append(row[0])  # If the value is not in the list, it will add to the list
        if line_count == 0:   # If this is the first row, it will print the column names
            print("Column names are: " + str(row))
            line_count += 1  # Increment the line count for each row read from the file
        line_count += 1
# Print the unique data values and the total number of lines processed
print(data)
print("Processed " + str(line_count) + " lines.")

# Uses os.path.join for constructing file paths
for i in data:  # Loops through data
    with open(combined_data_path) as combinedData_csv:    # Opens the combined data file
        csv_reader = csv.reader(combinedData_csv, delimiter=',')
        # Creates a file path for output file
        file_path = os.path.join(temp_dir, i[0:2] + ".csv")
        file = open(file_path, "w")   # Create and write to the output file
        file.write("scientificName,decimalLongitude,decimalLatitude\n")
        for row in csv_reader:
            if row[0] == i:
                string = ",".join(row)
                string = string + "\n"
                file.write(string)
        file.close()
    # Sets up parameters for creating shapefile
    in_Table = os.path.join(temp_dir, i[0:2] + ".csv")
    x_coords = "decimalLongitude"
    y_coords = "decimalLatitude"
    out_Layer = "CombinedData"
    saved_Layer = os.path.join(temp_dir, i[0:2] + ".shp")

    spRef = arcpy.SpatialReference(4326)
    # Creates an XY event layer and copy to shapefile
    lyr = arcpy.MakeXYEventLayer_management(in_Table, x_coords, y_coords, out_Layer, spRef, "")
    arcpy.CopyFeatures_management(lyr, saved_Layer)
    # Checks if shapefile was created successfully
    arcpy.CopyFeatures_management(lyr, saved_Layer)
    if arcpy.Exists(saved_Layer):
        print("Created file successfully!")
    # Gets the extent of shapefile
    desc = arcpy.Describe(saved_Layer)
    XMin = desc.extent.XMin
    XMax = desc.extent.XMax
    YMin = desc.extent.YMin
    YMax = desc.extent.YMax
    # Sets the output coordinate system
    arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(4326)
    # Defines the output shapefile path and name based on the input file name
    outFeatureClass = os.path.join(temp_dir, i[0:2] + "2.shp")

    # Calculates the minimum and maximum X coordinates of the input shapefile extent
    if XMin < 0:  # Checks if the minimum X coordinate is negative and adjust if necessary
        XMin_val = XMin * -1
    elif XMin >= 0:
        XMin_val = XMin

    if XMax < 0:  # Checks if the maximum X coordinate is negative and adjust if necessary
        XMax_val = XMax * -1
    elif XMax >= 0:
        XMax_val = XMax
    # Calculates the width of each cell in the fishnet
    cellSizeWidth = (XMin_val + XMax_val) / 80
    print(cellSizeWidth)
    # Sets other parameters for creating the fishnet
    originCoordinate = str(XMin) + " " + str(YMin)
    yAxisCoordinate = str(XMin) + " " + str(YMin + 1.0)
    cellSizeHeight = cellSizeWidth
    numRows = ""
    numColumns = ""
    oppositeCorner = str(XMax) + " " + str(YMax)
    labels = "NO_LABELS"
    templateExtent = "#"
    geometryType = "POLYGON"

    arcpy.CreateFishnet_management(outFeatureClass, originCoordinate, yAxisCoordinate,
                                   cellSizeWidth, cellSizeHeight, numRows, numColumns,
                                   oppositeCorner, labels, templateExtent, geometryType)
    # Creates the fishnet and print a message if successful
    if arcpy.Exists(outFeatureClass):
        print("Processing:" + i)
    # Sets parameters for the spatial join operation
    target_features = outFeatureClass
    join_features = saved_Layer
    out_feature_class = os.path.join(temp_dir, i[0:10] + "_HeatMap.shp")
    join_operation = "JOIN_ONE_TO_ONE"
    join_type = "KEEP_ALL"
    field_mapping = ""
    match_option = "INTERSECT"
    search_radius = ""
    distance_field_name = ""

    # Performs the spatial join and print a message if successful
    arcpy.SpatialJoin_analysis(target_features, join_features, out_feature_class,
                               join_operation, join_type, field_mapping, match_option,
                               search_radius, distance_field_name)

    if arcpy.Exists(out_feature_class):
        print("Created Heatmap file successfully!")
        print("Deleting intermediate files")

        # Removes intermediate files except for the output file

        intermediate_files = glob.glob(os.path.join(temp_dir, i[0:10] + "*.*"))
        for file in intermediate_files:
            if file != out_feature_class:
                os.remove(file)

# Move the output files to the desired output folder
output_folder = r"C:\Sip_EVS528\Sip_Coding_Challenge_07-main"
for file in glob.glob(os.path.join(temp_dir, "_HeatMap.shp")):
    shutil.move(file, os.path.join(output_folder, os.path.basename(file)))  # Attempting to use shutil because of many google searches

# Remove the temporary directory
shutil.rmtree(temp_dir)

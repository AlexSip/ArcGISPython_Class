# I will create a code where I can see buffers around wetlands in Rhode Island. I will make the buffers at 5 meters, but it
# really depends on what specific type of wetland I am working with. More information can be found on
# "Overview of Proposed Statewide Freshwater Wetland Regulation Revisions".pdf
# Basically, wetlands need a buffer to be determined so there can be a space to build and construct safely. My second
# part of the code will focus the wetland's buffer in South Kingstown, RI.
# NOTE: I put all the Data (Town and Wetland files) with my .py file in my directory

import os
import arcpy
arcpy.env.overwriteOutput = True  # This overwrites files when running/saving to prevent crashing

Directory = r"C:\Sip_EVS528\Sip_Midterm"  # Determine to your directory. If data is downloaded in its own folder, specify directory by adding \(name of folder)
arcpy.env.workspace = Directory  # Set the workspace
outputDirectory = os.path.join(Directory, "Temp_buffer")  # Creates a temporary folder
if not os.path.exists(outputDirectory):  # Checks if folder exists
    os.mkdir(outputDirectory)  # Creates the folder in the directory

arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(4326)  # Sets all output Spatial reference to WGS84

# This tool will create a 5meter buffer for wetlands shape file

in_features = r"wetlands.shp"  # Wetland shapefile used for buffer
out_feature_class = os.path.join(outputDirectory, "wetlands_5_meters.shp")  # Joins path components
buffer_distance_or_field = "5 meter"  # Specifying 5meters to buffer
line_side = "FULL"
line_end_type = "ROUND"
dissolve_option = "NONE"
dissolve_field = "#"
method = "PLANAR"

arcpy.analysis.Buffer(in_features, out_feature_class, buffer_distance_or_field, line_side, line_end_type, dissolve_option, dissolve_field, method)


if arcpy.Exists(out_feature_class):
    print("Wetland's Buffer File Has Been Successfully Created!")  # Check if file was created successfully

# This next tool is to create a new layer based on a selection by name in the towns shape file

inputFeature = "towns.shp"
outputFeature = os.path.join(outputDirectory, "SOUTH_KINGSTOWN.shp")
whereCategory = "NAME"  # Change selection category here, "NAME", it is case-sensitive
whereResponse = 'SOUTH KINGSTOWN'  # Change selection criteria here, 'SOUTH KINGSTOWN', it is case-sensitive
whereClause = "{} = '{}'".format(arcpy.AddFieldDelimiters(inputFeature, whereCategory), whereResponse)

arcpy.Select_analysis(inputFeature, outputFeature, whereClause)

if arcpy.Exists(outputFeature):
    print("South Kingstown Has Been Selected From Towns File Successfully!")  # Checks to see if the selection shapefile was created successfully

# Lastly, this tool will create an intersected layer of the Buffer and South Kingstown output

inputLayers = [out_feature_class, outputFeature]  # Declares a list variable that contains the paths of the input feature classes to be intersected.
outputLayer = os.path.join(outputDirectory, whereResponse + "WetlandIntersect.shp")
joinAttributes = "ALL"  # Combines all attributes from both tables into a new shapefile

arcpy.Intersect_analysis(inputLayers, outputLayer, joinAttributes)

if arcpy.Exists(outputLayer):
    print("Intersect file created successfully!\n")  # Prints a success message indicating that all files were created successfully

print("All files created successfully.\n")
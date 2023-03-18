# First import arcpy
import arcpy
# Follow the tool syntax
# Get shape file from my directory. You will have to change it to your specific directory for it to work
# do this by finding Dams.shp and right-clicking to copy path
in_features = r"C:\Sip_EVS528\Sip_CodingChallenge_04\Data\Dams.shp"
# Name the output in the directory
out_feature_class = r"C:\Sip_EVS528\Sip_CodingChallenge_04\Data\Dams_Output.shp"
# Specify Buffer
buffer_distance_or_field = "100 meter"
# using "#" to indicate non required field inputs
line_side = "#"
line_end_type = "#"
dissolve_option = "#"
dissolve_field = "#"
# Use method GEODESIC
method = "GEODESIC"
# Specify what is in Buffer tool, and run
arcpy.Buffer_analysis(in_features, out_feature_class, buffer_distance_or_field, line_side, line_end_type, dissolve_option, dissolve_field, method)
# Checks to see if the buffered shapefile was created successfully
if arcpy.Exists(out_feature_class):
    print ("Created file successfully!")

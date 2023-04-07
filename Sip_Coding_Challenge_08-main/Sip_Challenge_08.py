# For this challenge, I will create two functions from my previous codes

# This first function sets the workspace environment, lists the feature classes of the desired type, and performs a buffer
import arcpy

arcpy.env.overwriteOutput = True
def buffer_shapefile(in_features, out_feature_class, buffer_distance_or_field):
    # Specify non-required fields
    line_side = "#"
    line_end_type = "#"
    dissolve_option = "#"
    dissolve_field = "#"
    # Use method GEODESIC
    method = "GEODESIC"
    # Runs the Buffer tool
    arcpy.Buffer_analysis(in_features, out_feature_class, buffer_distance_or_field, line_side,
                          line_end_type, dissolve_option, dissolve_field, method)
    # Check if output file was created successfully
    if arcpy.Exists(out_feature_class):
        print("File was buffered successfully!")

in_features = r"C:\Sip_EVS528\Sip_Coding_Challenge_08-main\GIS_Dams\GIS_Dams\Dams.shp"
out_feature_class = r"C:\Sip_EVS528\Sip_Coding_Challenge_08-main\Dams_Output.shp"
buffer_distance_or_field = "100 meter"

buffer_shapefile(in_features, out_feature_class, buffer_distance_or_field)

# This second function converts polygon features to a raster dataset
def polygon_to_raster(in_features, val_field, out_raster, assignment_type, priority_field, cell_size):
    # Set environment settings
    arcpy.env.workspace = r"C:\Sip_EVS528\Sip_Coding_Challenge_08-main"

    # Runs PolygonToRaster
    arcpy.conversion.PolygonToRaster(in_features, val_field, out_raster, assignment_type, priority_field, cell_size)

    # Check if output raster was created successfully
    if arcpy.Exists(out_raster):
        print("Raster created successfully!")

in_features = r"C:\Sip_EVS528\Sip_Coding_Challenge_08-main\Towns\towns.shp"
val_field = "NAME"
out_raster = r"C:\Sip_EVS528\Sip_Coding_Challenge_08-main\Towns_raster"
assignment_type = "#"
priority_field = "#"
cell_size = 800

polygon_to_raster(in_features, val_field, out_raster, assignment_type, priority_field, cell_size)

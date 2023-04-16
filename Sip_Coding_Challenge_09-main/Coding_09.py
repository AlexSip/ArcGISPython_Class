import arcpy
arcpy.env.overwriteOutput = True
arcpy.env.workspace = r'C:\Sip_EVS528\Sip_Coding_Challenge_09-main\RI_Data'
input_shp = r'C:\Sip_EVS528\Sip_Coding_Challenge_09-main\RI_Data\RI_Forest_Health_Works_Project%3A_Points_All_Invasives.shp'

# Count how many individual records have photos
fields = ['PHOTO', 'Other']
expression = arcpy.AddFieldDelimiters(input_shp, "Other") + " = 'Photo' Or Other = 'Photos' Or Other = 'PHOTO'"

yes_photo = []
no_photo = []
count = 1

with arcpy.da.SearchCursor(input_shp, fields, expression) as cursor:
    for row in cursor:
        if row[0] not in yes_photo:
            yes_photo.append(row[0])
        count += 1

print("There are " + str(count - 1) + " individual records with photos, for the"
                  " following " + str(len(yes_photo)) + " sites:\n" + str(yes_photo))
# Generate shapefile with photos
in_layer_or_view = input_shp
selection_type = "NEW SELECTION"
where_clause = "Other = 'Photo' Or Other = 'Photos' Or Other = 'PHOTO'"
lyr = arcpy.management.SelectLayerByAttribute(in_layer_or_view, selection_type, where_clause)
cpy_lyr = 'RI_FHWP_invasives_pts_yesPhotos.shp'
arcpy.CopyFeatures_management(lyr, cpy_lyr)

if arcpy.Exists(cpy_lyr):
    print("Point shapefile has been successfully generated for records with photos.")
# Count of unique species there are in the dataset
fields = ['Species']
expression = arcpy.AddFieldDelimiters(input_shp, "Species") + " NOT LIKE ' %'"
sp_list = []

with arcpy.da.SearchCursor(input_shp, fields, expression) as cursor:
    for row in cursor:
        if row[0] not in sp_list:
            sp_list.append(row[0])

print("There are " + str(len(sp_list)) +
      " unique species in the dataset:\n" + str(sp_list))

# Individual records that do not have photos
expression = arcpy.AddFieldDelimiters(input_shp, "Other") + " <> 'Photo' And Other <> 'Photos' And Other <> 'PHOTO'"
no_photo = []
count = 1

with arcpy.da.SearchCursor(input_shp, fields, expression) as cursor:
    for row in cursor:
        if row[0] not in no_photo:
            no_photo.append(row[0])
        count += 1

print("There are " + str(count - 1) + " individual records without photos, for the"
                  " following " + str(len(no_photo)) + " sites:\n" + str(no_photo))
# Generate shapefile without photos
in_layer_or_view = input_shp
selection_type = "NEW SELECTION"
where_clause = "Other <> 'Photo' And Other <> 'Photos' And Other <> 'PHOTO'"
lyr = arcpy.management.SelectLayerByAttribute(in_layer_or_view, selection_type, where_clause)
cpy_lyr = 'RI_FHWP_invasives_pts_noPhotos.shp'
arcpy.CopyFeatures_management(lyr, cpy_lyr)

if arcpy.Exists(cpy_lyr):
    print("Point shapefile has been successfully generated for records without photos.")
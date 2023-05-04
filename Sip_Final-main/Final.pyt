# For my Final toolbox, I will create a toolbox that will consist of three tools ( Buffer, Dissolve and Clip)

import arcpy  # Import the arcpy library

arcpy.env.overwriteOutput = True  # Set overwrite output to True, which allows existing files to be overwritten

# Define a custom toolbox
class Toolbox(object):
    def __init__(self):
        self.label = "Road Toolbox"  # Set the toolbox label
        self.alias = ""  # Set the toolbox alias (not used in this example)
        self.tools = [Buffer, Dissolve, Clip]  # Define the tools that will be part of the toolbox

# Define a custom tool for buffering
class Buffer(object):
    def __init__(self):
        self.label = "1. Buffer Roads"  # Set the tool label
        self.description = "This tool will take up to three feature class objects and apply a 10-meter buffer."  # Set the tool description
        self.canRunInBackground = False  # Set whether the tool can be run in the background

    # Define the tool parameters
    def getParameterInfo(self):
        parameters = []
        shp1 = arcpy.Parameter(name="shp1",  # Set the parameter name
                               displayName="Enter your first shapefile:",  # Set the parameter display name
                               datatype="DEFeatureClass",  # Set the parameter data type
                               parameterType="Required",  # Set whether the parameter is required
                               direction="Input")  # Set the parameter direction
        parameters.append(shp1)  # Add the parameter to the list of parameters
        shp1_output = arcpy.Parameter(name="shp1_output",
                                      displayName="Enter the output destination for the first buffered shapefile:",
                                      datatype="DEFeatureClass",
                                      parameterType="Required",
                                      direction="Output")
        parameters.append(shp1_output)

        return parameters  # Return the list of parameters

    def isLicensed(self):
        return True  # Set whether the tool requires a license

    def updateParameters(self, parameters):
        return  # Define any updates to the tool parameters

    def updateMessages(self, parameters):
        return  # Define any updates to the tool messages

    def execute(self, parameters, messages):
        # Define the inputs and outputs for the Buffer tool
        shp1 = parameters[0].valueAsText
        shp1_output = parameters[1].valueAsText
        inputFeatures = shp1
        outputFeatures = shp1_output
        distance = "10 meters"
        sideType = "FULL"
        lineEndType = "ROUND"
        dissolveOption = "NONE"
        dissolveField = "#"
        method = "PLANAR"
        # Execute the Buffer tool with the defined inputs and outputs
        arcpy.Buffer_analysis(inputFeatures, outputFeatures, distance, sideType,
                              lineEndType, dissolveOption, dissolveField, method)
        arcpy.AddMessage("Buffering of files completed!")  # Add a message to the tool results
        return  # Return from the tool function

#DISSOLVE TOOL
class Dissolve(object):
    def __init__(self):
        # Initialize the Dissolve class with a label, description, and ability to run in the background.
        self.label = "2. Dissolve Roads"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        # Define the input and output parameters for the Dissolve tool.
        params = []
        input_features = arcpy.Parameter(name="input_features",
                                          displayName="Input Features",
                                          datatype="DEFeatureClass",
                                          parameterType="Required",
                                          direction="Input")
        params.append(input_features)
        dissolve_field = arcpy.Parameter(name="dissolve_field",
                                          displayName="Dissolve Field",
                                          datatype="Field",
                                          parameterType="Optional",
                                          direction="Input")
        params.append(dissolve_field)
        output_feature_class = arcpy.Parameter(name="out_feature_class",
                                               displayName="Output Feature Class",
                                               datatype="DEFeatureClass",
                                               parameterType="Required",
                                               direction="Output")
        params.append(output_feature_class)
        return params

    def isLicensed(self):
        # Check if the required ArcGIS license is available.
        return True

    def updateParameters(self, parameters):
        # Allow updating of parameters if needed.
        return

    def updateMessages(self, parameters):
        # Allow updating of messages if needed.
        return

    def execute(self, parameters, messages):
        # Run the Dissolve tool with the specified parameters and display messages about the output.
        input_features = parameters[0].valueAsText
        dissolve_field = parameters[1].valueAsText
        output_feature_class = parameters[2].valueAsText
        arcpy.AddMessage("Dissolving features...")
        arcpy.management.Dissolve(input_features,
                                  output_feature_class,
                                  dissolve_field,
                                  "",
                                  "MULTI_PART",
                                  "DISSOLVE_LINES")
        if arcpy.Exists(output_feature_class):
            arcpy.AddMessage("Successfully dissolved road  buffer zone.")
        desc = arcpy.Describe(output_feature_class)
        arcpy.AddMessage("File Path = " + str(desc.path))
        arcpy.AddMessage("Shape Type = " + str(desc.shapeType))
        arcpy.AddMessage(
            "Extent = XMin: {0}, XMax: {1}, YMin: {2}, YMax: {3}".format(desc.extent.XMin, desc.extent.XMax,
                                                                         desc.extent.YMin, desc.extent.YMax))
        arcpy.AddMessage("Coordinate System name = " + str(desc.spatialReference.name))
        arcpy.AddMessage("Coordinate System type = " + str(desc.spatialReference.type))
        return

# CLIP TOOL
class Clip(object):
    def __init__(self):
        # Initialize the Clip class with a label, description, and ability to run in the background.
        self.label = "3. Clip Roads"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        # Define the input and output parameters for the Clip tool.
        params = []
        input_features = arcpy.Parameter(name="input_features",
                                         displayName="Input Features",
                                         datatype="Feature Layer",
                                         parameterType="Required",
                                         direction="Input",
                                         )
        params.append(input_features)

        clip_features = arcpy.Parameter(name="clip_features",
                                         displayName="Clip Features",
                                         datatype="Feature Layer",
                                         parameterType="Required",
                                         direction="Input",
                                         )
        params.append(clip_features)

        output_feature_class = arcpy.Parameter(name="out_feature_class",
                                                displayName="Output Feature Class",
                                                datatype="DEFeatureClass",
                                                parameterType="Required",
                                                direction="Output",
                                                )
        params.append(output_feature_class)

        xy_tolerance = arcpy.Parameter(name="xy_tolerance",
                                        displayName="XY Tolerance",
                                        datatype="Linear Unit",
                                        parameterType="Optional",
                                        direction="Input"
                                        )
        xy_tolerance.value = "0.001 Miles"
        params.append(xy_tolerance)

        return params

    def isLicensed(self):
        # Check if the required ArcGIS license is available.
        return True

    def updateParameters(self, parameters):
        # Allow updating of parameters if needed.
        return

    def updateMessages(self, parameters):
        # Allow updating of messages if needed.
        return

    def execute(self, parameters, messages):
        # Run the Clip tool with the specified parameters and display messages about the output.
        input_features = parameters[0].valueAsText
        clip_features = parameters[1].valueAsText
        output_feature_class = parameters[2].valueAsText
        xy_tolerance = parameters[3].valueAsText

        arcpy.AddMessage("Clipping Roads...")
        arcpy.analysis.Clip(input_features, clip_features, output_feature_class, xy_tolerance)

        if arcpy.Exists(output_feature_class):
            arcpy.AddMessage("Successfully created clipped Roads.")

        desc = arcpy.Describe(output_feature_class)
        arcpy.AddMessage("File Path = " + str(desc.path))
        arcpy.AddMessage("Shape Type = " + str(desc.shapeType))
        arcpy.AddMessage(
            "Extent = XMin: {0}, XMax: {1}, YMin: {2}, YMax: {3}".format(desc.extent.XMin, desc.extent.XMax,
                                                                         desc.extent.YMin, desc.extent.YMax))
        arcpy.AddMessage("Coordinate System name = " + str(desc.spatialReference.name))
        arcpy.AddMessage("Coordinate System type = " + str(desc.spatialReference.type))
        return

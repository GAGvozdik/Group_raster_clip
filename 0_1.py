import os
import arcpy
from arcpy import env
from arcpy.sa import *

input = arcpy.GetParameterAsText(0) + "/"
contour = arcpy.GetParameterAsText(1)
output = arcpy.GetParameterAsText(2) + "/"

i = 0

for root, dirs, files in os.walk(input):
    for filename in files:
        if ((str(filename[-4:]) == '.tif') or (str(filename[-4:]) == '.flt')):
            arcpy.Clip_management(
                input + filename,
                "#",
                output + filename[:-4] + ".tif",
                contour,
                "0",
                "ClippingGeometry")
        i += 1
        if i > len(files):
            break
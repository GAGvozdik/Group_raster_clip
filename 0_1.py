import os
import arcpy
from arcpy import env
from arcpy.sa import *


input = arcpy.GetParameterAsText(0) + "/"
contour = arcpy.GetParameterAsText(1)
output = arcpy.GetParameterAsText(2) + "/"

# input = "C:/Users/fenik/Desktop/RAN/GroupTIFFcut/Group_raster_clip/input/"
# contour = "C:/Users/fenik/Desktop/RAN/GroupTIFFcut/Group_raster_clip/contour.shp"
# output = "C:/Users/fenik/Desktop/RAN/GroupTIFFcut/Group_raster_clip/output/"


if os.path.exists(output):
    for f in os.listdir(output):
        os.remove(os.path.join(output, f))

i = 0
end_var = []
for root, dirs, files in os.walk(input):
    for filename in files:
        if str(filename[-4:]) == '.tif':

            end_var.append(files[i])

            arcpy.Clip_management(
                input + filename,
                "#",
                output + filename[:-4] + "_cliped" + filename[-4:],
                contour,
                "0",
                "ClippingGeometry")
            print 'grd2'

        i += 1
        if i > len(files):
            break
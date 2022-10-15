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




i = 0
end_var = []




for root, dirs, files in os.walk(input):
    for filename in files:
        if str(filename[-4:]) == '.tif':

            end_var.append(files[i])

            for root1, dirs1, files1 in os.walk(output):
                for filename1 in files1:

                    n = output + filename[:-4] + "_cliped.tif"
                    if filename1 == n[len(output):]:
                        os.remove(n)

                    n = output + filename[:-4] + "_cliped.tif.aux.xml"
                    if filename1 == n[len(output):]:
                        os.remove(n)

                    n = output + filename[:-4] + "_cliped.tif.ovr"
                    if filename1 == n[len(output):]:
                        os.remove(n)

                    n = output + filename[:-4] + "_cliped.tfw"
                    if filename1 == n[len(output):]:
                        os.remove(n)

                    n = output + filename[:-4] + "_cliped.tif.xml"
                    if filename1 == n[len(output):]:
                        os.remove(n)

            for root1, dirs1, files1 in os.walk(output):
                for filename1 in files1:
                    if filename1 == output + filename[:-4] + "_cliped" + filename[-4:]:
                        n = output + filename[:-4] + "_cliped" + filename[-4:]
                        os.remove(n)
                        n = output + filename[:-4] + "_cliped.tif.aux.xml"
                        os.remove(n)
                        n = output + filename[:-4] + "_cliped.tif.ovr"
                        os.remove(n)

                        n = output + filename[:-4] + "_cliped.tfw"
                        os.remove(n)
                        n = output + filename[:-4] + "_cliped.tif.ovr"
                        os.remove(n)
                        n = output + filename[:-4] + "_cliped.tif.xml"
                        os.remove(n)
                        print "gg"


            arcpy.Clip_management(
                input + filename,
                "#",
                output + filename[:-4] + "_cliped" + filename[-4:],
                contour,
                "0",
                "ClippingGeometry")


        i += 1
        if i > len(files):
            break
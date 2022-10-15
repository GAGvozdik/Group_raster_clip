import os
import arcpy
from arcpy import env
from arcpy.sa import *





#
input = arcpy.GetParameterAsText(0) + "/"
contour = arcpy.GetParameterAsText(1)
output = arcpy.GetParameterAsText(2) + "/"

# input = "C:/Users/fenik/Desktop/000_ANTON/"
# contour = "C:/Users/fenik/Desktop/000_ANTON/contour.shp"
# output = "C:/Users/fenik/Desktop/000_ANTON/output/"




if os.path.exists(output):
    for f in os.listdir(output):
        os.remove(os.path.join(output, f))




i = 0
c = 0
end_var = []
for root, dirs, files in os.walk(input):
    for filename in files:

        if str(filename[-4:]) == '.tif':

            end_var.append(files[i])
            print end_var


            for j in end_var:
                l = 0
                if filename == j:
                    l+=1
                    break

            if l == 1 :
                break

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
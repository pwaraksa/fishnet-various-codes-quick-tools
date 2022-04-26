import arcpy
import numpy as np

# fc = r'D:\Hycza_treetops_\treetops_all_intersect.shp'
fc = r"D:\Projekt_Hycza\Analiza_NN_ripley\Analiza_rozmieszczenia\Points_intersect.shp"
fields1 = ['FID_BDL']

# For each row, print the WELL_ID and WELL_TYPE fields, and
# the feature's x,y coordinates
list1 = []
with arcpy.da.SearchCursor(fc, fields1) as cursor:
    for row in cursor:
        list1.append(row[0])
# print(list1)
#list1.sort()
#print(list1)
# print(list1[0],list1[1],list1[2])

fields2 = ['area']
list2 = []
with arcpy.da.SearchCursor(fc, fields2) as cursor:
    for row in cursor:
        list2.append(row[0])

# print(list2[0],list2[1],list2[2])


# function to get unique values 
# def unique(list):
#     x = np.array(list)
#     y= np.unique(x)
#     print(y[0])
#     return y
#
#
# unique_list1 = unique(list1)
# print(len(unique_list1))
#
# unique_list2 = unique(list2)
# print(len(unique_list2))

#Remove any duplicates from a List:
uniq_poly = list(dict.fromkeys(list1))
print("liczba poligonów: {}".format(len(uniq_poly)))

uniq_area = list(dict.fromkeys(list2))
print("liczba pow. poligonów: {}".format(len(uniq_area)))

#print("polygon_no, observed mean distance, expected mean distance, nearest neighbor index, z-score, p-value")

file = open("ANN_SUMMARY.txt","w")
line = "polygon_no, observed mean distance, expected mean distance, nearest neighbor index, z-score, p-value"
file.write(line + "\n")


for i in range(len(uniq_poly)):
    print(uniq_poly[i])

    # percent = round((i+1)*100/len(uniq_poly),2)
    # print("polygon number: {} ({}/{}, {}%)".format(uniq_poly[i],i+1,len(uniq_poly),percent))
    # print("polygon area: {}".format(uniq_area[i]))
    #
    # polygon_no = uniq_poly[i]
    # sql = '"FID_BDL" = {}'.format(polygon_no)
    #
    # # part_poly = arcpy.SelectLayerByAttribute_management(r"D:\Hycza_treetops_\treetops_all_intersect.shp", 'NEW_SELECTION', sql)
    # part_poly = arcpy.SelectLayerByAttribute_management(r"D:\Projekt_Hycza\Analiza_NN_ripley\Analiza_rozmieszczenia\Points_intersect.shp", 'NEW_SELECTION', sql)
    
    try:
        # nn_output = arcpy.AverageNearestNeighbor_stats(part_poly, "EUCLIDEAN_DISTANCE", "NO_REPORT", uniq_area[i])


        # line = "{},{},{},{},{},{}".format(polygon_no,nn_output[4],nn_output[3],nn_output[0],nn_output[1],nn_output[2])
        line = str(uniq_poly[i])
        # print(line)
        file.write(line + "\n")

        
    except arcpy.ExecuteError:
    # If an error occurred when running the tool, print out the error message.
        #print(arcpy.GetMessages())
        line = "{},NA,NA,NA,NA,NA".format(polygon_no)
        # print(line)
        file.write(line + "\n")

file.close()

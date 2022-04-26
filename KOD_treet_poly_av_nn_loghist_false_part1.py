import arcpy
import numpy as np
import datetime
import os

#filename number
filename = os.path.basename(__file__)
index = len(filename)-4
print()
N = int(filename[index])-1

fc = r"D:\Hycza_treetops_\12.11.2020\Analiza_rozmieszczenia\Points_intersect.shp"
fields1 = ['FID_BDL']

list1 = []
with arcpy.da.SearchCursor(fc, fields1) as cursor:
    for row in cursor:
        list1.append(row[0])

fields2 = ['area']
list2 = []
with arcpy.da.SearchCursor(fc, fields2) as cursor:
    for row in cursor:
        list2.append(row[0])



uniq_poly = list(dict.fromkeys(list1))
print("liczba poligonów: {}".format(len(uniq_poly)))

# uniq_area = list(dict.fromkeys(list2))
pol_area_dict = dict(zip(list1, list2))
uniq_area = []
for a in range(len(uniq_poly)):
    uniq_area.append(pol_area_dict[uniq_poly[a]])
print("liczba pow. poligonów: {}".format(len(uniq_area)))



#print("FID_BDL, observed mean distance, expected mean distance, nearest neighbor index, z-score, p-value")

file = open("CEGIELKA_DO_DOKTORATU_nn_popr_part{}.txt".format(N+1),"w")
line = "FID_BDL, observed mean distance, expected mean distance, nearest neighbor index, z-score, p-value"
file.write(line + "\n")

arcpy.SetLogHistory(False)


r1 = range(0,641)
r2 = range(641,1281)
r3 = range(1281,1921)
r4 = range(1921,2561)
r5 = range(2561,3201)
r6 = range(3201,3841)
r7 = range(3841,4481)
r8 = range(4481,5121)
r9 = range(5121,5761)
r10 = range(5761,6401)
rlist = (r1,r2,r3,r4,r5,r6,r7,r8,r9,r10)


for i in rlist[N]:

    per = round((640 - (rlist[N][640] - i)) * 100 / 640, 2)
    #percent = round((i+1)*100/412,2)
    print("polygon number: {} ({}/{}, {}%)".format(uniq_poly[i],i+1,rlist[N][640],per))
    print("polygon area: {}".format(uniq_area[i]))
    print(datetime.datetime.now())

    FID_BDL = uniq_poly[i]
    sql = '"FID_BDL" = {}'.format(FID_BDL)

    part_poly = arcpy.SelectLayerByAttribute_management(r"D:\Hycza_treetops_\12.11.2020\Analiza_rozmieszczenia\Points_intersect.shp", 'NEW_SELECTION', sql)
    
    try:
        nn_output = arcpy.AverageNearestNeighbor_stats(part_poly, "EUCLIDEAN_DISTANCE", "NO_REPORT", uniq_area[i])

#         Create list of Average Nearest Neighbor output values by splitting the result object
#         print("observed mean distance: " + nn_output[4])
#         print("expected mean distance: " + nn_output[3])
#         print("nearest neighbor index: " + nn_output[0])
#         print("z-score: " + nn_output[1])
#         print("p-value: " + nn_output[2])
#         print("path of the HTML: " + nn_output[5])
#         print("observed mean distance, expected mean distance, nearest neighbor index, z-score, p-value")
        
        line = "{},{},{},{},{},{}".format(FID_BDL,nn_output[4],nn_output[3],nn_output[0],nn_output[1],nn_output[2])
        # print(line)
        file.write(line + "\n")

        
    except arcpy.ExecuteError:
    # If an error occurred when running the tool, print out the error message.
        #print(arcpy.GetMessages())
        line = "{},NA,NA,NA,NA,NA".format(FID_BDL)
        # print(line)
        file.write(line + "\n")

file.close()

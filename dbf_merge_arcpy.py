import arcpy
import sys
sys.path.insert(1, r'C:\miniconda3\lib\site-packages')
# import dbfread
from dbfread import DBF



fc = r'D:\Hycza_treetops_\Project\Poprawne_wmk_od_Kroka\treetops_all_intersect_qgis2.shp'
fields1 = ['polyg_no']

list1 = []
with arcpy.da.SearchCursor(fc, fields1) as cursor:
    for row in cursor:
        list1.append(row[0])

uniq_poly = list(dict.fromkeys(list1))
print("liczba poligonów: {}".format(len(uniq_poly)))



file = open("CEGIELKA_DO_DOKTORATU_K_Ripley_popr.txt", "w")
line = "polygon_no, ExpectedK, ObservedK, DiffK"
file.write(line + "\n")


for i in range(len(uniq_poly)):

    percent = round((i+1)*100/len(uniq_poly),2)
    print("polygon number: {} ({}/{}, {}%)".format(uniq_poly[i],i+1,len(uniq_poly),percent))

    try:
        path = "D:\Hycza_fishnet\k_ripley_output\k_ripley_{}.dbf".format(uniq_poly[i])

        table = DBF(path, load=True)
        # print(table.records)
        # print(table.records[0]['Field1'])
        # print(table.records[0]['ExpectedK'])
        # print(table.records[0]['ObservedK'])
        # print(table.records[0]['DiffK'])

        line = "{},{},{},{}".format(uniq_poly[i],table.records[0]['ExpectedK'],table.records[0]['ObservedK'],table.records[0]['DiffK'])
        # print(line)
        file.write(line + "\n")
    except:
        line = "{},NA,NA,NA".format(uniq_poly[i])
        # print(line)
        file.write(line + "\n")


file.close()

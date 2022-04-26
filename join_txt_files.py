r = range(1,7)

# filename = "D:\Hycza_fishnet\CEGIELKA_DO_DOKTORATU_part{}.txt".format(r[i])
# list = []
output_file = open("CEGIELKA_DO_DOKTORATU_nn_popr_all_parts.txt", "w")

head = "FID_ID, observed mean distance, expected mean distance, nearest neighbor index, z-score, p-value"
output_file.write(head + "\n")

for i in r:
    # print(i)
    input_file_path = "D:\Projekt_Hycza\Analiza_NN_ripley\CEGIELKA_DO_DOKTORATU_nn_popr_part{}.txt".format(i)
    input_file = open(input_file_path,"r")
    # print(t.readline())
    m = input_file.readlines()
    print(type(m))

    for line in m[1:]:
        output_file.write(line)
        #output_file.write(line + "\n")
        # list.append(line)

output_file.close()


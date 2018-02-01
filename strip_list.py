file = open('vet.txt', 'r')

temp_list = []
temp_dict = {}
for line in file:
    line = line.strip().split(",")
    temp_list.append(line[0])
    temp_dict[line[0]] = line[1]

file.close()

temp_set = set(temp_list)
unique_new = list(temp_set)


file_agg = open('agg_list.txt', 'r')

for line in file_agg:
    line = line.strip().split(",")
    unique_new.append(line[0])
    temp_dict[line[0]] = line[1]

temp_set2 = set(unique_new)
unique_list_final = list(temp_set2)

file_clear_agg = open('agg_list.txt', 'w')
#file_clear_agg.write("Username," + "Name," + "Match? Y/N," + "," + "Success Rate")
#file_clear_agg.write("\n")
file_clear_agg.close()
unique_dict_final = {}
for element in unique_list_final:
    file_agg2 = open('agg_list.txt', 'a')
    file_agg2.write(element + "," + temp_dict[element])
    file_agg2.write('\n')
    file_agg2.close()


file_clear = open('vet.txt', 'w')
file_clear.close()

print(len(unique_list_final), "total unique hits")

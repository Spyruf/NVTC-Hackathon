import csv

def run():
    filetxt = open('for_heatmap.txt', 'r')

    lines = filetxt.readlines()
    filetxt.close()

    mycsv = csv.writer(open('f_heat.csv', 'w'))

    for line in lines:
        line = line.strip().split(",")
        mycsv.writerow(line)

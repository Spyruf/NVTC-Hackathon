import real_vet_heatmap

file = open('vet_pop_real.txt', 'r')
line = (file.readline()).split(",")
variables = []
for element in line:
    variables.append(element.strip())
#print(variables)

#for x in range(2, len(variables)):
number = 31
#title = ((variables[number].replace("_", " ")).title() + " Percentage")
title = ("Veteran Suicides Rate")
axes = ("Suicides per 100,000 Veterans")
real_vet_heatmap.run('vet_pop_real.txt', number, title, axes)
#print(title)
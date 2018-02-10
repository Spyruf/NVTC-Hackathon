file = open('agg_list.txt', 'r')

count = 0
for line in file:
    count = count + 1

print(str(count) + " total unique users")

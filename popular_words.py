import collections


file = open('words.txt', 'r')
all_words = []
casual_words = ['the', 'and', 'of', 'in', 'a', 'for', 'and', '&amp;', 'to', 'i', 'my', '|', '-']
detect = ["veteran", "navy", "marine", "guard", "usmc", "seals", "pilot", "#usaf", "#usnavy", "army",
                      "#usmarines", "#usarmy", "usmcvet", "medic", "trooper", "technician", "duty", "vietnam", "gulf",
                      "iran", "iraq", "colonel", "gysgt", "sgt", "sergeant", "platoon", "drill", "infantry", "vet",
                      "paramedic", "paratrooper"]
for line in file:
    line = line.strip().split(' ')
    for element in line:
        if len(element) > 0:
            if element.lower() not in casual_words:
                #if element.lower() not in detect:
                    all_words.append(element.lower())

counter = collections.Counter(all_words)
#print(counter)
print(counter.most_common(10))
#print(all_words)

#form a list of confirmed vets to feed into word_check


def run(file_name):
    file_name = file_name + ".txt"
    file = open(file_name, 'r')
    file.readline()

    confirmed_list = []
    for line in file:
        line = line.strip().split()
        #print(line)
        try:
            if line[-1] == "1":
                confirmed_list.append(line[0])
        except IndexError:
            print('dne')

    return confirmed_list
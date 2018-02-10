from __future__ import print_function
import collections

def run():
    popdensity = {
    'New Jersey':  0.0,
    'Rhode Island':   0.0,
    'Massachusetts':   0.0,
    'Connecticut':	  0.0,
    'Maryland':   0.0,
    'New York':    0.0,
    'Delaware':    0.0,
    'Florida':     0.0,
    'Ohio':	 0.0,
    'Pennsylvania':	 0.0,
    'Illinois':    0.0,
    'California':  0.0,
    'Hawaii':  0.0,
    'Virginia':    0.0,
    'Michigan':    0.0,
    'Indiana':    0.0,
    'North Carolina':  0.0,
    'Georgia':     0.0,
    'Tennessee':   0.0,
    'New Hampshire':   0.0,
    'South Carolina':  0.0,
    'Louisiana':   0.0,
    'Kentucky':   0.0,
    'Wisconsin':  0.0,
    'Washington':  0.0,
    'Alabama':     0.0,
    'Missouri':    0.0,
    'Texas':   0.0,
    'West Virginia':   0.0,
    'Vermont':     0.0,
    'Minnesota':  0.0,
    'Mississippi':	 0.0,
    'Iowa':	 0.0,
    'Arkansas':    0.0,
    'Oklahoma':    0.0,
    'Arizona':     0.0,
    'Colorado':    0.0,
    'Maine':  0.0,
    'Oregon': 0.0,
    'Kansas':  0.0,
    'Utah':	 0.0,
    'Nebraska':    0.0,
    'Nevada':  0.0,
    'Idaho':   0.0,
    'New Mexico':  0.0,
    'South Dakota':	 0.0,
    'North Dakota':	 0.0,
    'Montana':    0.0,
    'Wyoming':    0.0,
    'Alaska':    0.0}

    popwords = {
    'New Jersey':  [],
    'Rhode Island':   [],
    'Massachusetts':   [],
    'Connecticut':	  [],
    'Maryland':   [],
    'New York':    [],
    'Delaware':    [],
    'Florida':     [],
    'Ohio':	 [],
    'Pennsylvania':	 [],
    'Illinois':    [],
    'California':  [],
    'Hawaii':  [],
    'Virginia':    [],
    'Michigan':    [],
    'Indiana':    [],
    'North Carolina':  [],
    'Georgia':     [],
    'Tennessee':   [],
    'New Hampshire':   [],
    'South Carolina':  [],
    'Louisiana':   [],
    'Kentucky':   [],
    'Wisconsin':  [],
    'Washington':  [],
    'Alabama':     [],
    'Missouri':    [],
    'Texas':   [],
    'West Virginia':   [],
    'Vermont':     [],
    'Minnesota':  [],
    'Mississippi':	 [],
    'Iowa':	 [],
    'Arkansas':    [],
    'Oklahoma':    [],
    'Arizona':     [],
    'Colorado':    [],
    'Maine':  [],
    'Oregon': [],
    'Kansas':  [],
    'Utah':	 [],
    'Nebraska':    [],
    'Nevada':  [],
    'Idaho':   [],
    'New Mexico':  [],
    'South Dakota':	 [],
    'North Dakota':	 [],
    'Montana':    [],
    'Wyoming':    [],
    'Alaska':    []}

    stt = open('us_states.txt', 'r')
    abb_to_state = {}
    States = []

    for line in stt:
        line = line.strip().split("\t")
        abb_to_state[line[1]] = line[0]
        States.append(line[0].title())
    stt.close()

    stt1 = open('us_states2.txt', 'r')
    state_to_abb = {}
    for line in stt1:
        line = line.strip().split("\t")
        stNm = line[0].title()
        state_to_abb[stNm] = line[1]
    stt1.close()


    States = list(set(States))

    raw_file = open('location.txt', 'r')
    location_list = []
    for line in raw_file:
        line = line.strip()
        if len(line) > 0:
            location_list.append(line)

    lost = 0
    for element in location_list:
        hit = 0
        sep = element.split(",")
        bio = []
        if sep[-1] != "none":
            bio = sep[-1].split(" ")
        element = element.strip(" |.,/")
        if element.title() in popdensity:                                     #IF LOCATION IS DIRECTLY STATED (i.e. "Virginia")
            popdensity[element.title()] = popdensity[element.title()] + 1
            if len(bio) > 0:
                for word in bio:
                    (popwords[element.title()]).append(word)
            hit = 1
        elif "," in element:                                                  #IF LOCATION IS GIVEN WITH COMMAS (i.e. "Charlottesville, VA")
            element = element.split(",")
            for e in element:
                e = e.strip()
                if e.title() in popdensity:
                    popdensity[e.title()] = popdensity[e.title()] + 1
                    if len(bio) > 0:
                        for word in bio:
                            (popwords[e.title()]).append(word)
                    hit = 1
                elif e.upper() in abb_to_state:
                    state = abb_to_state[e.upper()]
                    popdensity[state.title()] = popdensity[state.title()] + 1
                    if len(bio) > 0:
                        for word in bio:
                            (popwords[state.title()]).append(word)
                    hit = 1
        elif " " in element:                                                 #IF LOCATION IS GIVEN WITH SPACE (i.e. "Charlottesville VA")
            element = element.split(" ")
            for e in element:
                e = e.strip()
                if e.title() in popdensity:
                    popdensity[e.title()] = popdensity[e.title()] + 1
                    if len(bio) > 0:
                        for word in bio:
                            (popwords[e.title()]).append(word)
                    hit = 1
                elif e.upper() in abb_to_state:
                    state = abb_to_state[e.upper()]
                    popdensity[state.title()] = popdensity[state.title()] + 1
                    if len(bio) > 0:
                        for word in bio:
                            (popwords[state.title()]).append(word)
                    hit = 1
        elif element.upper() in abb_to_state:                                       #IF LOCATION IS GIVEN WITH ABB (i.e. "VA")
            state = abb_to_state[element.upper()]
            popdensity[state.title()] = popdensity[state.title()] + 1
            if len(bio) > 0:
                for word in bio:
                    (popwords[state.title()]).append(word)
            hit = 1
        elif "/" in element:                                                  #IF LOCATION IS GIVEN WITH COMMAS (i.e. "Charlottesville/VA")
            element = element.split("/")
            for e in element:
                e = e.strip()
                if e.title() in popdensity:
                    popdensity[e.title()] = popdensity[e.title()] + 1
                    if len(bio) > 0:
                        for word in bio:
                            (popwords[e.title()]).append(word)
                    hit = 1
                elif e.upper() in abb_to_state:
                    state = abb_to_state[e.upper()]
                    popdensity[state.title()] = popdensity[state.title()] + 1
                    if len(bio) > 0:
                        for word in bio:
                            (popwords[state.title()]).append(word)
                    hit = 1
        if hit == 0:
            lost = lost + 1

    casual_words = ['the', 'and', 'of', 'in', 'a', 'for', 'and', '&amp;', 'to', 'i', 'my', '|', '-', '•', 'like', '--',
                    '||', '&', 'am', 'not', 'im', 'you', 'vet', 'get', 'have', 'as', 'is', 'with', 'at', 'if', 'youre',
                    "you're", "i'm", 'are', 'no', '', 'it', 'or', "don't", '1', '4', 'me', 'our', 'did', 'all', 'from',
                    "***", 'do', 'so', 'veteran', 'we', 'will', 'ab', 'by', 'on']
    file = open('for_heatmap.txt', 'w')
    file.write("CODE,STATE,COUNT,WORDS\n")
    file.close()

    total = 0
    for st in States:
        all_words = []
        fileTemp = open('for_heatmap.txt', 'a')
        counter = popwords[st]
        for element in counter:
            if len(element) > 0:
                if element.lower().strip(" /,.')(\"") not in casual_words:
                    all_words.append(element.title().strip(" ,.-')(\"").replace('-', ' '))

        found = collections.Counter(all_words)
        mostCommon = found.most_common(4)
        freq = popdensity[st]
        fileTemp.write(state_to_abb[st] + ",")
        fileTemp.write(st + ",")
        fileTemp.write(str(freq) + ",")
        for element in mostCommon:
            if element[1] > 20:
                print(st + ": " + element[0] + " " + str(element[1]))
                fileTemp.write(element[0] + "; ")
        fileTemp.write("\n")
        fileTemp.close
        total = total + freq

    print(str(total) + " hits")

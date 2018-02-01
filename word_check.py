import urllib.request
import re
import vet_confirms

file = open('words.txt', 'w')
file.close()
file_rwrt = open('conf_vet_list.txt', 'w')
file_rwrt.close()
#users = []
#for line in file:
#    line = line.split(",")
#    users.append(line[0])

f_names = ['twtv3', 'twtv2', 'twtv1', 'twtv4', 'twtv5']
for f in f_names:
    users = vet_confirms.run(f)

    for u in users:
        file_add_conf = open('conf_vet_list.txt', 'a')
        file_add_conf.write(u + "\n")

    for user in users:
        twitter_url = ("https://twitter.com/" + user)
        try:
            stream = urllib.request.urlopen(twitter_url)

            my_regex = """'[(]@""" + str(user) + """[)].', ([\S\s]+)>']"""
            #print(my_regex)

            find_bio = re.compile(my_regex)      #r"'[(]@erinmcunningham[)].', ([\S\s]+)>']"
            bio_found = ""
            for line in stream:
                line = str(line.decode("utf-8").strip().split())

                bio = re.search(find_bio, str(line))
                if bio:
                    #print(bio[1])
                    bio_found = bio[1].split(',')

            words = []
            for element in bio_found:
                e = element.strip(""" "',.@""")
                if len(e) > 0:
                    words.append(e)

            for word in words:
                file_add = open('words.txt', 'a')
                no_go = ["&amp;", 'the', 'and', 'of', 'in', 'a', 'for', 'and', '&amp;',
                         'to', 'i', 'my', '|']
                try:
                    if str(word) not in no_go:
                        word = str(word).replace("&#39;", "'")
                        file_add.write((str(word)).title() + " ")
                except UnicodeEncodeError:
                    print("ErrorUnicode")
                file_add.close()

            file_add = open('words.txt', 'a')
            file_add.write('\n')
            file_add.close()
        except urllib.error.HTTPError:
            print("ErrorHTTP: " + str(user))

        #print(words)

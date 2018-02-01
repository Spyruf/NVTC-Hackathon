from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


def run():
    consumer_key = "YAqvHGeTN46ttmmn8qyvtegSl"
    consumer_secret = "ssDGUf9jyYPsN5JCwrWH1IWA64LaUd9vsTPrd0J0Jm2gkpKURl"
    access_token = "3496798512-LgOl2NRjP0P7aX8XcqRV5c7yUMeJvS6njMJWNcc"
    access_token_secret = "5ApzTKHzk1aZ8rgxqNmEBPEVsxplqOfsKtlBiBx0K9adU"

    class listener(StreamListener):
        def on_data(self, data):
            detect = ["veteran", "navy", "marine", "usmc", "#usaf", "#usnavy", "#usmarines", "#usarmy", "usmcvet",
                      "#usmcvet", "colonel", "gysgt", "sgt", "sergeant",  "infantry", "vet", "paratrooper"]              #get more words to match profiles

            no_go_words = ["mom", "dad", "father", "mother", "grandma", "brat", "son", "daughter", "bts", "oc", "wife",
                           "wife"]

            all_data = json.loads(data)
            #print(all_data)

            try:
                bio = all_data["user"]["description"]
                username = all_data["user"]["screen_name"]
                name = all_data["user"]["name"]

                twt_words = bio
                count = 0
                if type(twt_words) == str:
                    wrd_temp = twt_words.split(" ")
                    wrd = []
                    for elmnt in wrd_temp:
                        wrd.append(elmnt.lower())

                    for words in wrd:
                        for words_d in detect:
                            if words.lower() == words_d.lower():
                                for neg in no_go_words:
                                    if neg not in wrd:
                                        count = count + 1
                                        if count == len(no_go_words):
                                            out = open('vet.txt', 'a')
                                            out.write(username + ",")
                                            try:
                                                out.write(name)
                                            except UnicodeEncodeError:
                                                out.write("n/a")
                                            out.write('\n')
                                            out.close()
                                            #print(type(twt_words))
                                            #print(" ")

                return True

            except KeyError:
                return True

        def on_error(self, status):
            print(status)

    twt_word_dtct = ["#VeteransForKaepernick", "#veterans", "#Veterans", "#2A", "2nd", "government", "USA", "army",
                     "navy", "marine", "#maga", "god", "veteran", "Veterans", "Army", "conservative", "Semper",
                     "gun", "the"]
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    twitterStream = Stream(auth, listener())
    twitterStream.filter(track=twt_word_dtct, languages=["en"])

run()

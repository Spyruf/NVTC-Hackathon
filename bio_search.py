from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from textblob import TextBlob

import json
import csv

total_tweets = 0
good_tweets = 0
neutral_tweets = 0
bad_tweets = 0


def flattenjson(b, delim):
    val = {}
    for i in b.keys():
        if isinstance(b[i], dict):
            get = flattenjson(b[i], delim)
            for j in get.keys():
                val[i + delim + j] = get[j]
        else:
            val[i] = b[i]

    return val


def get_tweet_sentiment(tweet):
    '''
    Utility function to classify sentiment of passed tweet
    using textblob's sentiment method
    '''
    # create TextBlob object of passed tweet text
    analysis = TextBlob(tweet)
    # set sentiment
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'


def run():
    consumer_key = "YAqvHGeTN46ttmmn8qyvtegSl"
    consumer_secret = "ssDGUf9jyYPsN5JCwrWH1IWA64LaUd9vsTPrd0J0Jm2gkpKURl"
    access_token = "3496798512-LgOl2NRjP0P7aX8XcqRV5c7yUMeJvS6njMJWNcc"
    access_token_secret = "5ApzTKHzk1aZ8rgxqNmEBPEVsxplqOfsKtlBiBx0K9adU"

    class listener(StreamListener):

        def on_data(self, data):
            detect = ["veteran", "navy", "marine", "usmc", "#usaf", "#usnavy", "#usmarines", "#usarmy", "usmcvet",
                      "#usmcvet", "colonel", "gysgt", "sgt", "sergeant", "infantry", "vet",
                      "paratrooper"]  # get more words to match profiles

            no_go_words = ["mom", "dad", "father", "mother", "grandma", "brat", "son", "daughter", "bts", "oc", "wife",
                           "wife"]

            all_data = json.loads(data)

            # print(all_data)
            # flat = flattenjson(all_data, '')
            # print(json.dumps(flat, indent=4, sort_keys=True))

            try:
                bio = all_data["user"]["description"]
                username = all_data["user"]["screen_name"]
                name = all_data["user"]["name"]
                location = all_data["user"]["location"]
                tweet = all_data["text"]

                # columns = ["BIO", "USERNAME", "NAME", "LOCATION", "TWEET", "SENTIMENT"]
                # myData = [["first_name", "second_name", "Grade"],
                #           ['Alex', 'Brian', 'A'],
                #           ['Tom', 'Smith', 'B']]
                # #
                # sentdata = open("sentiment_data.csv", 'w', newline='')
                # csv_w = csv.writer(sentdata)
                # csv_w.writerow(columns)
                #
                # # sentdata.close()

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

                                            sentfile = open("sent.txt", 'a')
                                            tweetfile = open("tweets.txt", 'a')
                                            locfile = open("sent_loc.txt", 'a')

                                            # user is valid
                                            sent = get_tweet_sentiment(tweet)
                                            global total_tweets
                                            global good_tweets
                                            global bad_tweets
                                            global neutral_tweets
                                            total_tweets += 1

                                            sent_value = int

                                            if sent is "positive":
                                                all_data["sentiment"] = 1
                                                sent_value = 1
                                                good_tweets += 1
                                            elif sent is "negative":
                                                all_data["sentiment"] = -1
                                                sent_value = -1
                                                bad_tweets += 1
                                            elif sent is "neutral":
                                                all_data["sentiment"] = 0
                                                sent_value = 0
                                                neutral_tweets += 1
                                            else:
                                                break
                                            print("------------------------------")
                                            print("Total Tweets:", total_tweets)
                                            print("Good Tweets:", (good_tweets / total_tweets) * 100)
                                            print("Neutral Tweets:", (neutral_tweets / total_tweets) * 100)
                                            print("Bad Tweets:", (bad_tweets / total_tweets) * 100)
                                            try:
                                                locfile.write("\n" + location + " : " + str(all_data["sentiment"]))
                                            except Exception as ex:
                                                print(ex)
                                            sentfile.write("\n------------------------------")
                                            sentfile.write("\nTotal Tweets:" + str(total_tweets))
                                            sentfile.write(
                                                "\nGood Tweets:" + str((good_tweets / total_tweets) * 100))
                                            sentfile.write(
                                                "\nNeutral Tweets:" + str((neutral_tweets / total_tweets) * 100))
                                            sentfile.write("\nBad Tweets:" + str((bad_tweets / total_tweets) * 100))

                                            tweetfile.write("\n------------------------------\n")
                                            tweetfile.write(tweet)

                                            sentfile.close()
                                            tweetfile.close()
                                            locfile.close()

                                            # ----------------

                                            # sentdata = open("sentiment_data.csv",'w', newline='')

                                            # columns = ["BIO", "USERNAME", "NAME", "LOCATION", "TWEET", "SENTIMENT"]
                                            # print("-------- writing to csv ----------")
                                            # print([bio, username, name, location, tweet,
                                            #        all_data["sentiment"]])
                                            #
                                            # myData = [bio, username, name, location, tweet,
                                            #           all_data["sentiment"]]
                                            #
                                            # csv_w.writerow()
                                            #
                                            # csv_w.writerow([bio, username, name, location, tweet,
                                            #                 all_data["sentiment"]])

                                            # input = map(lambda x: flattenjson(x, "__"), all_data)
                                            # columns = [x for row in input for x in row.keys()]
                                            # columns = list(set(columns))
                                            #
                                            # with sentdata as out_file:
                                            #     csv_w = csv.writer(out_file)
                                            #     csv_w.writerow(columns)
                                            #
                                            #     for i_r in input:
                                            #         csv_w.writerow(map(lambda x: i_r.get(x, ""), columns))

                                            # with sentdata:
                                            #     writer = csv.writer(sentdata)
                                            #     writer.writerows(flat)
                                            #
                                            # print("Writing complete")

                                            # sentdata.close()

                                            out = open('vet.txt', 'a')
                                            out2 = open('location.txt', 'a')
                                            out.write(username + ",")
                                            if type(location) == str:
                                                try:
                                                    out2.write(location)
                                                    try:
                                                        out2.write("," + bio.replace(",", " "))
                                                    except UnicodeEncodeError:
                                                        out2.write(',none')
                                                except UnicodeEncodeError:
                                                    out2.write('')
                                            # except TypeError or UnicodeEncodeError:
                                            #    out2.write('')
                                            try:
                                                out.write(name)
                                            except UnicodeEncodeError:
                                                out.write('n/a')
                                            out.write('\n')
                                            out2.write('\n')
                                            out.close()
                                            # print(type(twt_words))
                                            # print(" ")

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

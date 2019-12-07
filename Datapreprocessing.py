import json
import simplejson as json
import csv
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer



analyser = SentimentIntensityAnalyzer()

def sentiment_score(sentence):
	snt = analyser.polarity_scores(sentence)
	return snt

# headers = ['INDEX', 'TIMESTAMP', 'TWEET', 'USER NAME', 'ID', 'USER LOCATION', 'USER DESCRIPTION', 'FOLLOWER COUNT', 'VERIFIED STATUS', 'FRIENDS COUNT', 'STATUSES COUNT', 'CREATION TIME', 'GEO ENABLED', 'LOCATION', 'REPLY COUNT', 'RETWEET COUNT', 'LIKE COUNT', 'HASHTAGS', 'USERS MENTIONED SCREENNAME', 'USERS MENTIONED NAME', 'USERS MENTIONED ID', 'RETWEETED', 'FAVORITED', 'LANGUAGE', 'SEARCHTAG']
x = 1

data = []
# with open('dataset.csv', 'a') as csvfile:
#     csv.DictWriter(csvfile, fieldnames=headers).writeheader()
tweets_filename = './Dataset/denver.txt'
tweets_file = open(tweets_filename, 'r')




# OldMax = 1
# OldMin = -1
# NewMax = 10
# NewMin = 0
# OldRange = (OldMax - OldMin)
# NewRange = (NewMax - NewMin)

for line in tweets_file:
    try:
        tweet = json.loads(line.strip())
        if 'text' in tweet:
            content = {}
            content['created_at'] = ""
            content['text'] = ""
            content['user'] = {}
            content['user']['name'] = ""
            content['user']['screenname'] = ""
            content['user']['location'] = ""
            content['user']['description'] = ""
            content['user']['follower_count'] = ""
            content['user']['verified'] = ""
            content['user']['friends_count'] = ""
            content['user']['statuses_count'] = ""
            content['user']['created_at'] = ""
            content['user']['geo_enabled'] = ""
            content['place'] = ""
            content['reply_count'] = ""
            content['retweet_count'] = ""
            content['favorite_count'] = ""
            content['entities'] = {}
            content['entities']['hashtags'] = []
            # content['entities']['hashtags']['text'] = ""
            # content['entities']['user_mentions'] = {}
            # content['entities']['user_mentions']['screenname'] = []
            # content['entities']['user_mentions']['name'] = []
            # content['entities']['user_mentions']['id'] = []
            # content['entities']['user_mentions']['id_str'] = []
            content['favorited'] = ""
            content['retweeted'] = ""
            content['lang'] = ""
            content['searchtag'] = ""
            content['created_at'] = tweet['created_at']
            content['text'] = (tweet['text'])
            content['user']['name'] = (tweet['user']['name'])
            content['user']['screenname'] = tweet['user']['screen_name']
            content['user']['location'] = (tweet['user']['location'])
            content['user']['description'] = (tweet['user']['description'])
            content['user']['follower_count'] = (tweet['user']['followers_count'])
            content['user']['verified'] = (tweet['user']['verified'])
            content['user']['friends_count'] = (tweet['user']['friends_count'])
            content['user']['statuses_count'] = (tweet['user']['statuses_count'])
            content['user']['created_at'] = (tweet['user']['created_at'])
            content['user']['geo_enabled'] = (tweet['user']['geo_enabled'])
            content['place'] = (tweet['place'])
            content['reply_count'] = (tweet['reply_count'])
            content['retweet_count'] = (tweet['retweet_count'])
            content['favorite_count'] = (tweet['favorite_count'])
            hashtags = {}
            hashtags['text'] = ""
            for hashtag in tweet['entities']['hashtags']:
                hashtags['text'] = hashtag['text']
                content['entities']['hashtags'].append(hashtags)
            # screenname = []
            # name = []
            # ids = []
            # id_str = [] 
            # for user in tweet['entities']['user_mentions']:
            #     screenname.append(user['screenname'])
            #     name.append(user['name'])
            #     ids.append(user['id'])
            #     id_str.append(user['id_str'])
            # content['entities']['user_mentions']['screenname'].append(screenname)
            # content['entities']['user_mentions']['name'].append(name)
            # content['entities']['user_mentions']['id'].append(ids)
            # content['entities']['user_mentions']['id_str'].append(id_str)
            content['retweeted'] = (tweet['retweeted'])
            content['favorited'] = (tweet['favorited'])
            content['lang'] = (tweet['lang'])
            ps = sentiment_score(content['text'])
            NewValue = (((ps['compound'] - OldMin) * NewRange) / OldRange) + NewMin
            content['severity_score'] = str(NewValue)
            content['searchtag'] = 'MINvsKC'

        
            # print(content)
            data.append(content)
            #with open('denver.txt', 'a') as outfile:
            #    json.dump(content, outfile)
            #     # print(content)
            # with open('dataset.csv', 'a') as csvfile:
                
            #     writer = csv.DictWriter(csvfile,fieldnames = headers)
                
            #     row = {'INDEX':x, 'TIMESTAMP':tweet['created_at'], 'TWEET':tweet['text'], 'USER NAME':tweet['user']['name'], 'ID':tweet['user']['screen_name'], 'USER LOCATION':tweet['user']['location'], 'USER DESCRIPTION':tweet['user']['description'], 'FOLLOWER COUNT':tweet['user']['followers_count'], 'VERIFIED STATUS':tweet['user']['verified'], 'FRIENDS COUNT':tweet['user']['friends_count'], 'STATUSES COUNT':tweet['user']['statuses_count'], 'CREATION TIME':tweet['user']['created_at'], 'GEO ENABLED':tweet['user']['geo_enabled'], 'LOCATION':tweet['place'], 'REPLY COUNT':tweet['reply_count'],'RETWEET COUNT':tweet['retweet_count'], 'LIKE COUNT':tweet['favorite_count'], 'HASHTAGS':tweet['entities']['hashtags']['text'], 'USERS MENTIONED SCREENNAME':screenname , 'USERS MENTIONED NAME':name , 'USERS MENTIONED ID':id_str, 'RETWEETED':tweet['retweeted'], 'FAVORITED':tweet['favorited'], 'LANGUAGE':tweet['lang'], 'SEARCHTAG':content['searchtag']}
            #     writer.writerow(row)
            #     x = x+1
            #     hashtags=[]
            #     for hashtag in tweet['entities']['hashtags']:
            #         hashtags.append(hashtag['text'])
            
            
    except:
        continue
    print(content)
# final_json.append(content)
# print(final_json)
# with open('kansas.txt', 'w') as outfile:
#     json.dump(data, outfile)
# print(data)
# json = []
# for line in data:
#     json.append(line)

    # json += line + "," 
# json = json[:-2]

# print(json)
# with open('datajsonfinal.txt', 'w') as f:
#     for item in data:
#         f.write("%s," % item)
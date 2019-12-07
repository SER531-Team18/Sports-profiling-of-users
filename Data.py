import json
import simplejson as json
import csv


headers = ['INDEX', 'TIMESTAMP', 'TWEET', 'USER NAME', 'ID', 'USER LOCATION', 'USER DESCRIPTION', 'FOLLOWERS COUNT', 'VERIFIED STATUS', 'FRIENDS COUNT', 'STATUSES COUNT', 'CREATION TIME', 'GEO ENABLED', 'LOCATION', 'REPLY COUNT', 'RETWEET COUNT', 'LIKE COUNT', 'RETWEETED', 'FAVORITED', 'HASHTAGS', 'LANGUAGE', 'TAG', 'SEVERITY-SCORE']
x = 1

with open('dataset.csv', 'a') as csvfile:
    csv.DictWriter(csvfile, fieldnames = headers).writeheader()
tweets_filename = 'denver.txt'
tweets_file = open(tweets_filename, 'r')



for line in tweets_file:
    try:
        tweet = json.loads(line.strip())
        for i in range(len(line)):
            print(tweet[i]['created_at'])
            print(tweet[i]['text'])
            print(tweet[i]['user']['name'])
            print(tweet[i]['user']['screenname'])
            print(tweet[i]['user']['location'])
            print(tweet[i]['user']['description'])
            print(tweet[i]['user']['follower_count'])
            print(tweet[i]['user']['verified'])
            print(tweet[i]['user']['friends_count'])
            print(tweet[i]['user']['statuses_count'])
            print(tweet[i]['user']['created_at'])
            print(tweet[i]['user']['geo_enabled'])
            print(tweet[i]['place'])
            print(tweet[i]['reply_count'])
            print(tweet[i]['retweet_count'])
            print(tweet[i]['favorite_count'])
            print(tweet[i]['retweeted'])
            print(tweet[i]['favorited'])
            print(tweet[i]['lang'])
            print(tweet[i]['searchtag'])
            print(tweet[i]['entities']['hashtags'])
            print(tweet[i]['severity_score'])
            with open('dataset.csv', 'a') as csvfile:
                
                writer = csv.DictWriter(csvfile,fieldnames = headers)
                
                row = {'INDEX':x, 'TIMESTAMP':tweet[i]['created_at'], 'TWEET':tweet[i]['text'], 'USER NAME':tweet[i]['user']['name'], 'ID':tweet[i]['user']['screenname'], 'USER LOCATION':tweet[i]['user']['location'], 'USER DESCRIPTION':tweet[i]['user']['description'], 'FOLLOWERS COUNT':tweet[i]['user']['follower_count'], 'VERIFIED STATUS':tweet[i]['user']['verified'], 'FRIENDS COUNT':tweet[i]['user']['friends_count'], 'STATUSES COUNT':tweet[i]['user']['statuses_count'], 'CREATION TIME':tweet[i]['user']['created_at'], 'GEO ENABLED':tweet[i]['user']['geo_enabled'], 'LOCATION':tweet[i]['place'], 'REPLY COUNT':tweet[i]['reply_count'],'RETWEET COUNT':tweet[i]['retweet_count'], 'LIKE COUNT':tweet[i]['favorite_count'], 'RETWEETED':tweet[i]['retweeted'], 'FAVORITED':tweet[i]['favorited'], 'HASHTAGS':tweet[i]['entities']['hashtags'],'LANGUAGE':tweet[i]['lang'], 'TAG':tweet[i]['searchtag'], 'SEVERITY-SCORE':tweet[i]['severity_score']}
                writer.writerow(row)
                x = x+1
            #     hashtags=[]
            #     for hashtag in tweet['entities']['hashtags']:
            #         hashtags.append(hashtag['text'])
            
            
    except:
        continue


tweets_filename = 'denver1.txt'
tweets_file = open(tweets_filename, 'r')



for line in tweets_file:
    try:
        tweet = json.loads(line.strip())
        for i in range(len(line)):
            print(tweet[i]['created_at'])
            print(tweet[i]['text'])
            print(tweet[i]['user']['name'])
            print(tweet[i]['user']['screenname'])
            print(tweet[i]['user']['location'])
            print(tweet[i]['user']['description'])
            print(tweet[i]['user']['follower_count'])
            print(tweet[i]['user']['verified'])
            print(tweet[i]['user']['friends_count'])
            print(tweet[i]['user']['statuses_count'])
            print(tweet[i]['user']['created_at'])
            print(tweet[i]['user']['geo_enabled'])
            print(tweet[i]['place'])
            print(tweet[i]['reply_count'])
            print(tweet[i]['retweet_count'])
            print(tweet[i]['favorite_count'])
            print(tweet[i]['retweeted'])
            print(tweet[i]['favorited'])
            print(tweet[i]['lang'])
            print(tweet[i]['searchtag'])
            print(tweet[i]['entities']['hashtags'])
            print(tweet[i]['severity_score'])
            with open('dataset.csv', 'a') as csvfile:
                
                writer = csv.DictWriter(csvfile,fieldnames = headers)
                
                row = {'INDEX':x, 'TIMESTAMP':tweet[i]['created_at'], 'TWEET':tweet[i]['text'], 'USER NAME':tweet[i]['user']['name'], 'ID':tweet[i]['user']['screenname'], 'USER LOCATION':tweet[i]['user']['location'], 'USER DESCRIPTION':tweet[i]['user']['description'], 'FOLLOWERS COUNT':tweet[i]['user']['follower_count'], 'VERIFIED STATUS':tweet[i]['user']['verified'], 'FRIENDS COUNT':tweet[i]['user']['friends_count'], 'STATUSES COUNT':tweet[i]['user']['statuses_count'], 'CREATION TIME':tweet[i]['user']['created_at'], 'GEO ENABLED':tweet[i]['user']['geo_enabled'], 'LOCATION':tweet[i]['place'], 'REPLY COUNT':tweet[i]['reply_count'],'RETWEET COUNT':tweet[i]['retweet_count'], 'LIKE COUNT':tweet[i]['favorite_count'], 'RETWEETED':tweet[i]['retweeted'], 'FAVORITED':tweet[i]['favorited'], 'HASHTAGS':tweet[i]['entities']['hashtags'],'LANGUAGE':tweet[i]['lang'], 'TAG':tweet[i]['searchtag'], 'SEVERITY-SCORE':tweet[i]['severity_score']}
                writer.writerow(row)
                x = x+1
            #     hashtags=[]
            #     for hashtag in tweet['entities']['hashtags']:
            #         hashtags.append(hashtag['text'])
            
            
    except:
        continue


tweets_filename = 'denver2.txt'
tweets_file = open(tweets_filename, 'r')



for line in tweets_file:
    try:
        tweet = json.loads(line.strip())
        for i in range(len(line)):
            print(tweet[i]['created_at'])
            print(tweet[i]['text'])
            print(tweet[i]['user']['name'])
            print(tweet[i]['user']['screenname'])
            print(tweet[i]['user']['location'])
            print(tweet[i]['user']['description'])
            print(tweet[i]['user']['follower_count'])
            print(tweet[i]['user']['verified'])
            print(tweet[i]['user']['friends_count'])
            print(tweet[i]['user']['statuses_count'])
            print(tweet[i]['user']['created_at'])
            print(tweet[i]['user']['geo_enabled'])
            print(tweet[i]['place'])
            print(tweet[i]['reply_count'])
            print(tweet[i]['retweet_count'])
            print(tweet[i]['favorite_count'])
            print(tweet[i]['retweeted'])
            print(tweet[i]['favorited'])
            print(tweet[i]['lang'])
            print(tweet[i]['searchtag'])
            print(tweet[i]['entities']['hashtags'])
            print(tweet[i]['severity_score'])
            with open('dataset.csv', 'a') as csvfile:
                
                writer = csv.DictWriter(csvfile,fieldnames = headers)
                
                row = {'INDEX':x, 'TIMESTAMP':tweet[i]['created_at'], 'TWEET':tweet[i]['text'], 'USER NAME':tweet[i]['user']['name'], 'ID':tweet[i]['user']['screenname'], 'USER LOCATION':tweet[i]['user']['location'], 'USER DESCRIPTION':tweet[i]['user']['description'], 'FOLLOWERS COUNT':tweet[i]['user']['follower_count'], 'VERIFIED STATUS':tweet[i]['user']['verified'], 'FRIENDS COUNT':tweet[i]['user']['friends_count'], 'STATUSES COUNT':tweet[i]['user']['statuses_count'], 'CREATION TIME':tweet[i]['user']['created_at'], 'GEO ENABLED':tweet[i]['user']['geo_enabled'], 'LOCATION':tweet[i]['place'], 'REPLY COUNT':tweet[i]['reply_count'],'RETWEET COUNT':tweet[i]['retweet_count'], 'LIKE COUNT':tweet[i]['favorite_count'], 'RETWEETED':tweet[i]['retweeted'], 'FAVORITED':tweet[i]['favorited'], 'HASHTAGS':tweet[i]['entities']['hashtags'],'LANGUAGE':tweet[i]['lang'], 'TAG':tweet[i]['searchtag'], 'SEVERITY-SCORE':tweet[i]['severity_score']}
                writer.writerow(row)
                x = x+1
            #     hashtags=[]
            #     for hashtag in tweet['entities']['hashtags']:
            #         hashtags.append(hashtag['text'])
            
            
    except:
        continue




tweets_filename = 'kansas.txt'
tweets_file = open(tweets_filename, 'r')



for line in tweets_file:
    try:
        tweet = json.loads(line.strip())
        for i in range(len(line)):
            print(tweet[i]['created_at'])
            print(tweet[i]['text'])
            print(tweet[i]['user']['name'])
            print(tweet[i]['user']['screenname'])
            print(tweet[i]['user']['location'])
            print(tweet[i]['user']['description'])
            print(tweet[i]['user']['follower_count'])
            print(tweet[i]['user']['verified'])
            print(tweet[i]['user']['friends_count'])
            print(tweet[i]['user']['statuses_count'])
            print(tweet[i]['user']['created_at'])
            print(tweet[i]['user']['geo_enabled'])
            print(tweet[i]['place'])
            print(tweet[i]['reply_count'])
            print(tweet[i]['retweet_count'])
            print(tweet[i]['favorite_count'])
            print(tweet[i]['retweeted'])
            print(tweet[i]['favorited'])
            print(tweet[i]['lang'])
            print(tweet[i]['searchtag'])
            print(tweet[i]['entities']['hashtags'])
            print(tweet[i]['severity_score'])
            with open('dataset.csv', 'a') as csvfile:
                
                writer = csv.DictWriter(csvfile,fieldnames = headers)
                
                row = {'INDEX':x, 'TIMESTAMP':tweet[i]['created_at'], 'TWEET':tweet[i]['text'], 'USER NAME':tweet[i]['user']['name'], 'ID':tweet[i]['user']['screenname'], 'USER LOCATION':tweet[i]['user']['location'], 'USER DESCRIPTION':tweet[i]['user']['description'], 'FOLLOWERS COUNT':tweet[i]['user']['follower_count'], 'VERIFIED STATUS':tweet[i]['user']['verified'], 'FRIENDS COUNT':tweet[i]['user']['friends_count'], 'STATUSES COUNT':tweet[i]['user']['statuses_count'], 'CREATION TIME':tweet[i]['user']['created_at'], 'GEO ENABLED':tweet[i]['user']['geo_enabled'], 'LOCATION':tweet[i]['place'], 'REPLY COUNT':tweet[i]['reply_count'],'RETWEET COUNT':tweet[i]['retweet_count'], 'LIKE COUNT':tweet[i]['favorite_count'], 'RETWEETED':tweet[i]['retweeted'], 'FAVORITED':tweet[i]['favorited'], 'HASHTAGS':tweet[i]['entities']['hashtags'],'LANGUAGE':tweet[i]['lang'], 'TAG':tweet[i]['searchtag'], 'SEVERITY-SCORE':tweet[i]['severity_score']}
                writer.writerow(row)
                x = x+1
            #     hashtags=[]
            #     for hashtag in tweet['entities']['hashtags']:
            #         hashtags.append(hashtag['text'])
            
            
    except:
        continue



tweets_filename = 'laker.txt'
tweets_file = open(tweets_filename, 'r')



for line in tweets_file:
    try:
        tweet = json.loads(line.strip())
        for i in range(len(line)):
            print(tweet[i]['created_at'])
            print(tweet[i]['text'])
            print(tweet[i]['user']['name'])
            print(tweet[i]['user']['screenname'])
            print(tweet[i]['user']['location'])
            print(tweet[i]['user']['description'])
            print(tweet[i]['user']['follower_count'])
            print(tweet[i]['user']['verified'])
            print(tweet[i]['user']['friends_count'])
            print(tweet[i]['user']['statuses_count'])
            print(tweet[i]['user']['created_at'])
            print(tweet[i]['user']['geo_enabled'])
            print(tweet[i]['place'])
            print(tweet[i]['reply_count'])
            print(tweet[i]['retweet_count'])
            print(tweet[i]['favorite_count'])
            print(tweet[i]['retweeted'])
            print(tweet[i]['favorited'])
            print(tweet[i]['lang'])
            print(tweet[i]['searchtag'])
            print(tweet[i]['entities']['hashtags'])
            print(tweet[i]['severity_score'])
            with open('dataset.csv', 'a') as csvfile:
                
                writer = csv.DictWriter(csvfile,fieldnames = headers)
                
                row = {'INDEX':x, 'TIMESTAMP':tweet[i]['created_at'], 'TWEET':tweet[i]['text'], 'USER NAME':tweet[i]['user']['name'], 'ID':tweet[i]['user']['screenname'], 'USER LOCATION':tweet[i]['user']['location'], 'USER DESCRIPTION':tweet[i]['user']['description'], 'FOLLOWERS COUNT':tweet[i]['user']['follower_count'], 'VERIFIED STATUS':tweet[i]['user']['verified'], 'FRIENDS COUNT':tweet[i]['user']['friends_count'], 'STATUSES COUNT':tweet[i]['user']['statuses_count'], 'CREATION TIME':tweet[i]['user']['created_at'], 'GEO ENABLED':tweet[i]['user']['geo_enabled'], 'LOCATION':tweet[i]['place'], 'REPLY COUNT':tweet[i]['reply_count'],'RETWEET COUNT':tweet[i]['retweet_count'], 'LIKE COUNT':tweet[i]['favorite_count'], 'RETWEETED':tweet[i]['retweeted'], 'FAVORITED':tweet[i]['favorited'], 'HASHTAGS':tweet[i]['entities']['hashtags'],'LANGUAGE':tweet[i]['lang'], 'TAG':tweet[i]['searchtag'], 'SEVERITY-SCORE':tweet[i]['severity_score']}
                writer.writerow(row)
                x = x+1
            #     hashtags=[]
            #     for hashtag in tweet['entities']['hashtags']:
            #         hashtags.append(hashtag['text'])
            
            
    except:
        continue




tweets_filename = 'newengland.txt'
tweets_file = open(tweets_filename, 'r')



for line in tweets_file:
    try:
        tweet = json.loads(line.strip())
        for i in range(len(line)):
            print(tweet[i]['created_at'])
            print(tweet[i]['text'])
            print(tweet[i]['user']['name'])
            print(tweet[i]['user']['screenname'])
            print(tweet[i]['user']['location'])
            print(tweet[i]['user']['description'])
            print(tweet[i]['user']['follower_count'])
            print(tweet[i]['user']['verified'])
            print(tweet[i]['user']['friends_count'])
            print(tweet[i]['user']['statuses_count'])
            print(tweet[i]['user']['created_at'])
            print(tweet[i]['user']['geo_enabled'])
            print(tweet[i]['place'])
            print(tweet[i]['reply_count'])
            print(tweet[i]['retweet_count'])
            print(tweet[i]['favorite_count'])
            print(tweet[i]['retweeted'])
            print(tweet[i]['favorited'])
            print(tweet[i]['lang'])
            print(tweet[i]['searchtag'])
            print(tweet[i]['entities']['hashtags'])
            print(tweet[i]['severity_score'])
            with open('dataset.csv', 'a') as csvfile:
                
                writer = csv.DictWriter(csvfile,fieldnames = headers)
                
                row = {'INDEX':x, 'TIMESTAMP':tweet[i]['created_at'], 'TWEET':tweet[i]['text'], 'USER NAME':tweet[i]['user']['name'], 'ID':tweet[i]['user']['screenname'], 'USER LOCATION':tweet[i]['user']['location'], 'USER DESCRIPTION':tweet[i]['user']['description'], 'FOLLOWERS COUNT':tweet[i]['user']['follower_count'], 'VERIFIED STATUS':tweet[i]['user']['verified'], 'FRIENDS COUNT':tweet[i]['user']['friends_count'], 'STATUSES COUNT':tweet[i]['user']['statuses_count'], 'CREATION TIME':tweet[i]['user']['created_at'], 'GEO ENABLED':tweet[i]['user']['geo_enabled'], 'LOCATION':tweet[i]['place'], 'REPLY COUNT':tweet[i]['reply_count'],'RETWEET COUNT':tweet[i]['retweet_count'], 'LIKE COUNT':tweet[i]['favorite_count'], 'RETWEETED':tweet[i]['retweeted'], 'FAVORITED':tweet[i]['favorited'], 'HASHTAGS':tweet[i]['entities']['hashtags'],'LANGUAGE':tweet[i]['lang'], 'TAG':tweet[i]['searchtag'], 'SEVERITY-SCORE':tweet[i]['severity_score']}
                writer.writerow(row)
                x = x+1
            #     hashtags=[]
            #     for hashtag in tweet['entities']['hashtags']:
            #         hashtags.append(hashtag['text'])
            
            
    except:
        continue



tweets_filename = 'newengland1.txt'
tweets_file = open(tweets_filename, 'r')



for line in tweets_file:
    try:
        tweet = json.loads(line.strip())
        for i in range(len(line)):
            print(tweet[i]['created_at'])
            print(tweet[i]['text'])
            print(tweet[i]['user']['name'])
            print(tweet[i]['user']['screenname'])
            print(tweet[i]['user']['location'])
            print(tweet[i]['user']['description'])
            print(tweet[i]['user']['follower_count'])
            print(tweet[i]['user']['verified'])
            print(tweet[i]['user']['friends_count'])
            print(tweet[i]['user']['statuses_count'])
            print(tweet[i]['user']['created_at'])
            print(tweet[i]['user']['geo_enabled'])
            print(tweet[i]['place'])
            print(tweet[i]['reply_count'])
            print(tweet[i]['retweet_count'])
            print(tweet[i]['favorite_count'])
            print(tweet[i]['retweeted'])
            print(tweet[i]['favorited'])
            print(tweet[i]['lang'])
            print(tweet[i]['searchtag'])
            print(tweet[i]['entities']['hashtags'])
            print(tweet[i]['severity_score'])
            with open('dataset.csv', 'a') as csvfile:
                
                writer = csv.DictWriter(csvfile,fieldnames = headers)
                
                row = {'INDEX':x, 'TIMESTAMP':tweet[i]['created_at'], 'TWEET':tweet[i]['text'], 'USER NAME':tweet[i]['user']['name'], 'ID':tweet[i]['user']['screenname'], 'USER LOCATION':tweet[i]['user']['location'], 'USER DESCRIPTION':tweet[i]['user']['description'], 'FOLLOWERS COUNT':tweet[i]['user']['follower_count'], 'VERIFIED STATUS':tweet[i]['user']['verified'], 'FRIENDS COUNT':tweet[i]['user']['friends_count'], 'STATUSES COUNT':tweet[i]['user']['statuses_count'], 'CREATION TIME':tweet[i]['user']['created_at'], 'GEO ENABLED':tweet[i]['user']['geo_enabled'], 'LOCATION':tweet[i]['place'], 'REPLY COUNT':tweet[i]['reply_count'],'RETWEET COUNT':tweet[i]['retweet_count'], 'LIKE COUNT':tweet[i]['favorite_count'], 'RETWEETED':tweet[i]['retweeted'], 'FAVORITED':tweet[i]['favorited'], 'HASHTAGS':tweet[i]['entities']['hashtags'],'LANGUAGE':tweet[i]['lang'], 'TAG':tweet[i]['searchtag'], 'SEVERITY-SCORE':tweet[i]['severity_score']}
                writer.writerow(row)
                x = x+1
            #     hashtags=[]
            #     for hashtag in tweet['entities']['hashtags']:
            #         hashtags.append(hashtag['text'])
            
            
    except:
        continue


tweets_filename = 'newyork.txt'
tweets_file = open(tweets_filename, 'r')



for line in tweets_file:
    try:
        tweet = json.loads(line.strip())
        for i in range(len(line)):
            print(tweet[i]['created_at'])
            print(tweet[i]['text'])
            print(tweet[i]['user']['name'])
            print(tweet[i]['user']['screenname'])
            print(tweet[i]['user']['location'])
            print(tweet[i]['user']['description'])
            print(tweet[i]['user']['follower_count'])
            print(tweet[i]['user']['verified'])
            print(tweet[i]['user']['friends_count'])
            print(tweet[i]['user']['statuses_count'])
            print(tweet[i]['user']['created_at'])
            print(tweet[i]['user']['geo_enabled'])
            print(tweet[i]['place'])
            print(tweet[i]['reply_count'])
            print(tweet[i]['retweet_count'])
            print(tweet[i]['favorite_count'])
            print(tweet[i]['retweeted'])
            print(tweet[i]['favorited'])
            print(tweet[i]['lang'])
            print(tweet[i]['searchtag'])
            print(tweet[i]['entities']['hashtags'])
            print(tweet[i]['severity_score'])
            with open('dataset.csv', 'a') as csvfile:
                
                writer = csv.DictWriter(csvfile,fieldnames = headers)
                
                row = {'INDEX':x, 'TIMESTAMP':tweet[i]['created_at'], 'TWEET':tweet[i]['text'], 'USER NAME':tweet[i]['user']['name'], 'ID':tweet[i]['user']['screenname'], 'USER LOCATION':tweet[i]['user']['location'], 'USER DESCRIPTION':tweet[i]['user']['description'], 'FOLLOWERS COUNT':tweet[i]['user']['follower_count'], 'VERIFIED STATUS':tweet[i]['user']['verified'], 'FRIENDS COUNT':tweet[i]['user']['friends_count'], 'STATUSES COUNT':tweet[i]['user']['statuses_count'], 'CREATION TIME':tweet[i]['user']['created_at'], 'GEO ENABLED':tweet[i]['user']['geo_enabled'], 'LOCATION':tweet[i]['place'], 'REPLY COUNT':tweet[i]['reply_count'],'RETWEET COUNT':tweet[i]['retweet_count'], 'LIKE COUNT':tweet[i]['favorite_count'], 'RETWEETED':tweet[i]['retweeted'], 'FAVORITED':tweet[i]['favorited'], 'HASHTAGS':tweet[i]['entities']['hashtags'],'LANGUAGE':tweet[i]['lang'], 'TAG':tweet[i]['searchtag'], 'SEVERITY-SCORE':tweet[i]['severity_score']}
                writer.writerow(row)
                x = x+1
            #     hashtags=[]
            #     for hashtag in tweet['entities']['hashtags']:
            #         hashtags.append(hashtag['text'])
            
            
    except:
        continue




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
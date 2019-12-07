import json
import csv
import string
import seaborn as sns
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import io
import shutil



def sentiment_score(sentence):
	snt = analyser.polarity_scores(sentence)
	return snt

analyser = SentimentIntensityAnalyzer()
w = 0
r = 1
b = 10
l = 0

#tweets_filename = '/Users/akhilesh/Desktop/Assignments/531/game_dataset/FINAL_JSON_GAME_DATASET.txt'
#tweets_file = open(tweets_filename, "r")

#input_file = open ('/Users/akhilesh/Desktop/FINAL_JSON_GAME_DATASET.txt')

file = open('/Users/akhilesh/Desktop/FINAL_JSON_GAME_DATASET.txt', 'r')
json1 = file.read()

json_array = json.loads(json1)
OldMax = 1
OldMin = -1
NewMax = 10
NewMin = 0
OldRange = (OldMax - OldMin)
NewRange = (NewMax - NewMin)

for item in json_array:
	#print(item['comment'])
	ps = sentiment_score(item['comment'])
	NewValue = (((ps['compound'] - OldMin) * NewRange) / OldRange) + NewMin
	#print("-------------")
	#print(item['comment'])
	#print("Severity Score: " + str(NewValue))
	#print("-------------")
	item['sevirity_score'] = str(NewValue)

with open('/Users/akhilesh/Desktop/SentimentAnalysisComplete.txt', 'w') as outfile:
	json.dump(json_array, outfile)

print(json_array)
'''
for line in tweets_file:
	print(line)
	print("---------")
	try:
		tweet = json.loads(line.strip())
		print(tweet)
		if 'comment' in tweet:
			print(tweet[comment])
			ps = sentiment_score(tweet['comment'])

			if ps['compound'] < 0:
				w = w + ps['compound']
				l = l+1

	except:
		continue
		'''


#k = (w/l)

def severity_score(y):

	sever = ((y) * b)/r
	#print("sever = ")
	#print(sever)
	#print("k = ")
	#print(k)
	#weighted for urgency
	weight = sever - k
	#print("weight = ")
	#print(weight)
	res = weight *sever

	#print("sever = ")
	x = res/10
	#print(x)
	y = round(x,1)
	#print(y)
	return y

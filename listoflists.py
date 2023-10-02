import re
import csv
import nltk
import pandas as pd
#start process_tweet
fl=0
nb=[]
sen=""
def processTweet(tweet):
	# process the tweets
	
	#Convert to lower case
	tweet = tweet.lower()
	#Convert www.* or https?://* to URL
	tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL',tweet)
	#Convert @username to AT_USER
	tweet = re.sub('@[^\s]+','AT_USER',tweet)    
	#Remove additional white spaces
	tweet = re.sub('[\s]+', ' ', tweet)
	#Replace #word with word
	tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
	#trim
	tweet = tweet.strip('\'"')
	return tweet

#Read the tweets one by one and process it
"""
fp = open('sampleTweets.txt', 'r')
line = fp.readline()

while line:
	processedTweet = processTweet(line)
	print(processedTweet)
	line = fp.readline()
#end loop
fp.close()
"""
stopWords = []

#start replaceTwoOrMore
def replaceTwoOrMore(s):
	#look for 2 or more repetitions of character and replace with the character itself
	pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
	return pattern.sub(r"\1\1", s)
#end

#start getStopWordList
def getStopWordList(stopWordListFileName):
	#read the stopwords file and build a list
	stopWords = []
	stopWords.append('AT_USER')
	stopWords.append('URL')

	fp = open(stopWordListFileName, 'r')
	line = fp.readline()
	while line:
		word = line.strip()
		stopWords.append(word)
		line = fp.readline()
	fp.close()
	return stopWords
#end

#start getfeatureVector
def getFeatureVector(tweet, stopWords):
	featureVector = []  
	words = tweet.split()
	for w in words:
		#replace two or more with two occurrences 
		w = replaceTwoOrMore(w) 
		#strip punctuation
		w = w.strip('\'"?,.')
		#check if it consists of only words
		val = re.search(r"^[a-zA-Z][a-zA-Z0-9]*[a-zA-Z]+[a-zA-Z0-9]*$", w)
		#ignore if it is a stopWord
		if(w in stopWords or val is None):
			continue
		else:
			featureVector.append(w.lower())
	return featureVector 
def extract_features(tweet):
	tweet_words = set(tweet)
	features = {}
	for word in featureList:
		features['contains(%s)' % word] = (word in tweet_words)
	return features
inpTweets = csv.reader(open('samplecsv.csv', 'r'), delimiter=',')
stopWords = getStopWordList('stopwords.txt')
count=0
featureList = []
# Get tweet words
tweets = []
for row in inpTweets:
	sentiment = row[0]
	tweet = row[1]
	processedTweet = processTweet(tweet)
	featureVector = getFeatureVector(processedTweet,stopWords)
	featureList.extend(featureVector)
	tweets.append((featureVector, sentiment));
#end loop
# Remove featureList duplicates
featureList = list(set(featureList))
# Extract feature vector for all tweets in one shote
training_set = nltk.classify.util.apply_features(extract_features, tweets)
NBClassifier = nltk.NaiveBayesClassifier.train(training_set)
with open('Test.csv','r', newline='',encoding="utf8") as infh:
	reader = csv.reader(infh)
	for row in reader:
		testTweet = row[2]
		processedTestTweet = processTweet(testTweet)
		exf=extract_features(getFeatureVector(processedTestTweet,stopWords))
		for ke,val in exf.items():
				if val==True:
					fl=1
		if(fl!=1):
			sen="neutral"
			nb.append(sen)
		else:
			sen=NBClassifier.classify(extract_features(getFeatureVector(processedTestTweet,stopWords)))
			nb.append(sen)
		print(processedTestTweet,sen)
		df = open('Test.csv','r',encoding="utf8")
		data = [item for item in csv.reader(df)]
		df.close()
		new_data=[]
		for it, item in enumerate(data):
			try:
				item.append(nb[it])
			except IndexError:
				item.append("placeholder")
			new_data.append(item)
		df = open('sentiment.csv', 'w',newline="",encoding="utf8")
		csv.writer(df).writerows(new_data)
		df.close()
feature_names = cv.get_feature_names()
train_set = []
for i, single_sample in enumerate(X):
    single_feature_dict = {}
    for j, single_feature in enumerate(single_sample):
        single_feature_dict[feature_names[j]]=single_feature
    train_set.append((single_feature_dict, y[i])) 
print("Classifier accuracy percent:",(nltk.classify.util.accuracy(NBClassifier,extract_features(getFeatureVector(processedTestTweet,stopWords)).items()))*100)
"""
with open('your_file.txt', 'w') as f:
	for item in extract_features(getFeatureVector(processedTestTweet,stopWords)):
		f.write("%s\t" % item)
		f.write("%s \n" %nb)
"""
# Test the classifier
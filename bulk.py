inpTweets = csv.reader(open('sampleTweets.csv', 'r',encoding="utf8"), delimiter=',', quotechar='|')
stopWords = getStopWordList('stopwords.txt')
featureList = []
# Get tweet words
tweets = []
for row in inpTweets:
    sentiment = row[0]
    tweet = row[1]
    processedTweet = processTweet(tweet)
    featureVector = getFeatureVector(processedTweet, stopWords)
    featureList.extend(featureVector)
    tweets.append((featureVector, sentiment));
#end loop
# Remove featureList duplicates
featureList = list(set(featureList))
# Extract feature vector for all tweets in one shote
training_set = nltk.classify.util.apply_features(extract_features, tweets)
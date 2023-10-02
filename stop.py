from nltk.corpus import stopwords
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize 
import csv
import pandas as pd
stop_words = set(stopwords.words('english'))
fs=[] 
with open('Test.csv', "r", encoding='utf8') as infile:
	read = csv.reader(infile)
	for row in read :
		#print (row[5])
		tweetsplit=row[2]
		word_tokens = word_tokenize(tweetsplit) 
		filtered_sentence = [w for w in word_tokens if not w in stop_words]
		s=""
		for w in word_tokens:
			if w not in stop_words:
				for i in filtered_sentence:
					if(i=="#" or i=="@" or i=="&"):
						index=filtered_sentence.index(i)
						del filtered_sentence[index:index+2]
				for tp in filtered_sentence:
					if(tp=="http" or tp=="https" or tp==":" or tp=="?" or tp=="/" or tp=="." or tp=="," or tp=="!" or tp==";" or tp=="%" or tp=="[" or tp=="]" or tp=="-" or tp=="+" or tp==")" or tp=="("):
						filtered_sentence.remove(tp)
				for ae in filtered_sentence:
					if ae.__contains__("//"):
						filtered_sentence.remove(ae)
		for ad in filtered_sentence:
			ind=filtered_sentence.index(ad)
			if filtered_sentence[ind]!=filtered_sentence[-1]:
				s=s+ad+","
			else:
				s=s+ad
		fs.append(s)
		print(s)
rows=zip(fs)
with open('sv.csv','w',newline="",encoding='utf8') as dest:
	wtr = csv.writer(dest)
	for row in rows:
		wtr.writerow(row)
"""
p=pd.read_csv('Test.csv')
ppp=pd.read_csv('sv.csv')
ppp[1]=p[2]
ppp.to_csv('sv.csv')
print(fs[1])
"""
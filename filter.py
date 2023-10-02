import csv
import pandas as pd
p=pd.read_csv('dataa.csv')
ppp=pd.read_csv('filtered.csv')
print(p['hashtags'])
ppp['hashtags']=p['hashtags']
ppp.to_csv('filtered.csv',header=False)

"""
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
with open("C:/Users/Rahul/Desktop/dataa.csv","r",encoding="utf8") as source:
    rdr= csv.reader(source)
    with open("C:/Users/Rahul/Desktop/filtered.csv","w",encoding="utf8") as result:
        wtr= csv.writer(result)
        for r in rdr:
            wtr.writerow((r[4],))
"""
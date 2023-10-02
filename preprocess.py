import nltk.classify
from nltk.corpus import movie_reviews
from nltk.corpus import opinion_lexicon
from nltk.corpus import stopwords
import stop
nltk.download('stopwords')
nltk.download('punkt')
from nltk.tokenize import word_tokenize


stop_words = stopwords.words("english")

def create_word_features_pos(words):
    useful_words = [word for word in words if word not in stop_words]
    my_list = [({word: True}, 'positive') for word in useful_words]
    return my_list


def create_word_features_neg(words):
    useful_words = [word for word in words if word not in stop_words]
    my_list = [({word: True}, 'negative') for word in useful_words]
    return my_list


def create_word_features(words):
    global a
    global prod
    prod=1
    useful_words = [word for word in words if word not in stopwords.words("english")]
    
    pos_txt = get_tokenized_file(u'positivewords.txt')
    neg_txt = get_tokenized_file(u'negativewords.txt')
    
    my_dict = dict([(word, 1) for word in pos_txt if word in useful_words])
    my_dict1 = dict([(word, -1) for word in neg_txt if word in useful_words])
    
    my_dict.update(my_dict1)
    for key in my_dict1:
        a=my_dict1[key]
        b=int(a)
        temp=prod*(b)
        prod=temp
    
    
    
    
    return my_dict

def get_tokenized_file(file):
    return word_tokenize(open(file, 'r').read())

def get_data():
	print("Collecting Negative Words")
	neg_txt = get_tokenized_file(u'negativewords.txt')
	neg_features = create_word_features_neg(neg_txt)

	print("Collecting Positive Words")
	pos_txt = get_tokenized_file(u'positivewords.txt')
	pos_features = create_word_features_pos(pos_txt)
	return pos_features + neg_features

def process(data):
    return [word.lower() for word in word_tokenize(data)]

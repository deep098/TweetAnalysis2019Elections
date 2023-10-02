from preprocess import create_word_features, create_word_features_neg
from preprocess import create_word_features_pos, process
from classifier import get_classifier
import stop
import nltk.classify
from tkinter import *
import preprocess


print("Designing UI")
root = Tk()
root.wm_title('Sentiment Analysis Application')

top_frame = Frame(root)
top_frame.pack()

bottom_frame = Frame(root)
bottom_frame.pack(side=BOTTOM)

l1 = Label(top_frame, text='Keywords:')
l1.pack(side=LEFT)
j=Label(top_frame, text=stop.fs[12])
j.pack(side=LEFT)

print("UI COMPLETE")
clf = get_classifier()

def main_op():
    #review_spirit = w.get('1.0',END)
    review_spirit = j.cget("text")
    
    demo = process(review_spirit)

    demo1 = create_word_features(demo)
    #demo2 = ('review is ' + clf.classify(demo1))
    
    demo2=('review value',preprocess.prod)
    l2 = Label(bottom_frame, text=demo2)
    l2.pack()

button = Button(bottom_frame, text='Analyse', command=main_op )
button.pack(side=BOTTOM)

root.mainloop()

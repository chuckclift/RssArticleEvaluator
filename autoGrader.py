#!/usr/bin/python

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
import pickle
import re


with open("content.txt") as c:
    content_text = c.read()

    titles = content_text.split("</title>")
    titles = titles[:-1]
    titles = [a.split("<title>")[1] for a in titles]

    texts = content_text.split("</article>")
    texts = texts[:-1]
    texts = [a.split("<article")[1] for a in texts] 

   

# The training data is in a list of tuples
# it is formatted like this
# (title, category, text)
ex_data = pickle.load(open("gradedArticles.pkl", "rb"))

ex_titles = [a[0] for a in ex_data]
ex_categories = [a[1] for a in ex_data]
ex_text = [a[2] for a in ex_data]

count_vect = CountVectorizer()
counts = count_vect.fit_transform(ex_text + texts)
tfidf_transformer = TfidfTransformer()
tfidf_data = tfidf_transformer.fit_transform(counts)


clf = MultinomialNB().fit(tfidf_data[:len(ex_text)], ex_categories)
predictions = []

for a in tfidf_data[len(ex_text):]:
    predicted_category = clf.predict(a)
    predictions.append(predicted_category)

for a, b  in zip(titles, predictions):
    print("Title: %s \nScore: %s\n " % (a, b[0]))


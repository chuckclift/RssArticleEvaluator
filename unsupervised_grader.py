#!/usr/bin/python3.4

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans, MiniBatchKMeans
import argparse
import nltk
import sys
from string import punctuation

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("h", type=str,  help="History file")
    args = parser.parse_args()

    headlines = [line for line in sys.stdin]

    with open(args.h) as history:
        old = [a for a in history]


    headline_scores = cluster_text(headlines, old,  20)
    print("Printing headlines")
    for h in headline_scores:
        print(h[0], h[1][:75])

def interesting_words(text):
    words = nltk.word_tokenize(text.lower())
    stopwords = nltk.corpus.stopwords.words('english')
    return " ".join([a for a in words if not a in stopwords])

def cluster_text(texts, old,  clusters):
    keywords = [interesting_words(a) for a in old + texts]
    interesting_headlines = [(a,b) for a,b in zip(texts, keywords) if b] 

    vectorizer = TfidfVectorizer(stop_words="english", use_idf=True)
    counts = vectorizer.fit_transform((a[1] for a in interesting_headlines))

    if len(interesting_headlines) > 10000:
        km = KMeans(n_clusters=clusters)   
    else:
        km = MiniBatchKMeans(n_clusters=clusters) 
    
    km.fit(

    matched = [(g,h[0]) for g,h in  zip(guess, interesting_headlines )]
    matched.sort()
    matched = [a for a in matched if a[1] in texts]
    return matched

if __name__=="__main__":
    main()

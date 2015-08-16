#!/usr/bin/python3.4

from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans, MiniBatchKMeans
import nltk
import optparse
import sys

def main():
    parser = optparse.OptionParser()
    parser.add_option("-f", action="store", default="",help="Input file")
    parser.add_option("-c", action="store", type="int", default=15,
                       help="The number of categories")
    parser.add_option("-o", action="store", default="", help="Output file")

    options, args = parser.parse_args()

    headlines = [line for line in sys.stdin]
    if options.f:
        with open(options.f) as i:
            headlines = i.read().split("\n")

    headlines = [" ".join(h.split()) for h in headlines]


    sys.stdout.write("\n".join([" ".join((str(i), sen)) for i, sen in cluster_text(headlines, options.c)]))

def important_words(text):
    words = nltk.word_tokenize(text)
    tags = nltk.pos_tag(words)

    return  " ".join([a[0] for a in tags 
                     if a[1]=="NN" or a[1]=="VBP" or a[1]=="JJ"])
    

def cluster_text(texts, clusters):
    keywords = [important_words(a) for a in texts]
    vectorizer = TfidfVectorizer(stop_words="english", use_idf=True)
    counts = vectorizer.fit_transform(keywords)

    km = KMeans(n_clusters=clusters)
    guess = km.fit_predict(counts)

    matched = [(guess[i],sent) for i, sent in enumerate(texts)]
    matched.sort()

    return matched.copy()

if __name__=="__main__":
    main()

#!/usr/bin/env python3

import nltk
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('keywords', help='The keywords used to grade the articles')
args = parser.parse_args()

keywords = set()
with open(args.keywords) as k:
    keywords = {''.join(a.split()) for a in k}

for line in sys.stdin:
    line = ' '.join(line.split())
    words = {a.lower() for a in  nltk.word_tokenize(line)}
    if words.intersection(keywords):
        print(line) 
   



import evaluator
import numpy
from sklearn.naive_bayes import MultinomialNB
from sklearn import svm

with open("classifierWords.txt") as f:
    classifierWords = f.read()
    classifierWords = classifierWords.split("\n")
    classifierWords = filter(None, classifierWords)
    classifierWords = [word.strip() for word in classifierWords]

with open("articles.txt") as g:
    articles = g.read()
        
    # cleans up the formatting, making it more readable
    articles = articles.replace("<article>", "")
    articles = articles.replace("   ", "")
    articles = articles.replace("\n", " ")


    # getting rid of the space after the last article
    last = articles.rfind("</article")
    articles = articles[:last]

# splitting articles into a list for processing in the upcoming loop
article_text_list = articles.split("</article>")
article_objects = []


for text in article_text_list:
    currentArticle = evaluator.Article(classifierWords, text)
    article_objects.append(currentArticle)

with open("csvData.csv") as c:
    rows = c.read().split("\n")
    rows = filter(None, rows)
    rows = [a for a in rows] # converting iterable back to list

    data = []
    results = []
    
    testing_values = []
    for r in rows:
        numbers = [float(n) for n in r.split(",")]
        data.append(numbers[0:-1])
        results.append(numbers[-1])

clf = svm.SVC(gamma=0.001, C=100)
clf.fit(data, results)

for article in article_objects:
    article_score = clf.predict(article.get_data())
    article.set_score(article_score)
    print(article.get_score())


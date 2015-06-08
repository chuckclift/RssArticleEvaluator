﻿from __future__ import division
import re

with open("classifierWords.txt") as f:
    classifierWords = f.read()
    classifierWords = classifierWords.split("\n")
    classifierWords = filter(None, classifierWords)
    classifierWords = [word.strip() for word in classifierWords]

with open("articles.txt") as g:
    articles = g.read()

LOWEST_GRADE = 1
HIGHEST_GRADE = 5
MAX_WORD_COUNT = 20


class Article(object):
    def __init__(self, searchKeywords, thisArticleText):
        self.searchKeywords = searchKeywords
        self.articleText = thisArticleText.replace("  ", "")
        self.keywordFrequencies = []

        for word in searchKeywords:
            count = 0
            regex = "[ \.\?\"\'!,]" + word + "[ \.\?\"\'!,s]"
            count = len(re.findall(regex, self.articleText.lower()))
            normalizedScore = count / MAX_WORD_COUNT
            self.keywordFrequencies.append(normalizedScore)

    def getText(self):
        return self.articleText

    def reportData(self):
        csv = ""
        for value in self.keywordFrequencies:
            csv = csv + str(value) + ","

        return csv


def makeCsv(articleObjList):
    finalCsv = ""
    counter = 0

    for articleOb in articleObjList:

        current = articleOb.getText()
        articleLength = len(current)

        while len(current) > 0:
            # prints out one line for the user to read

            try:
                print(current[:70])
            except UnicodeEncodeError:
                troubleString = current[:70].encode('utf-16')
                print("We're Doomed")

            current = current[70:]

            # every fifth line, it stops
            # and waits for the user to read
            counter += 1
            if counter is 5:
                counter = 0
                input("")
                # user presses enter to continue reading

                # after the user is done reading, he is asked
                # to assign a category.  It won't let him submit
                # an empty string so he doesn't accidentally
                # skip this part
        grade = ""

        question = ("Grade?("
                    + str(LOWEST_GRADE)
                    + "-"
                    + str(HIGHEST_GRADE)
                    + ")\n")

        while len(grade) is 0:

            grade = input(question)

            if len(grade) > 0:
                if int(grade) < LOWEST_GRADE:
                    grade = ""
                    print("Your number is too low\n")
                elif int(grade) > HIGHEST_GRADE:
                    grade = ""
                    print("Your number is too high\n")

        finished = input("Done?(y/n)\n")

        # Normalizing the data on the scale of zero to one
        grade = (int(grade) - LOWEST_GRADE) / (HIGHEST_GRADE - LOWEST_GRADE)

        finalCsv = finalCsv + articleOb.reportData() + str(grade) + "\n"

        if finished == "y":
            return finalCsv

    return finalCsv

# cleans up the formatting, making it more readable
articles = articles.replace("<article>", "")
articles = articles.replace("   ", "")
articles = articles.replace("\n", " ")

# getting rid of the space after the last article
last = articles.rfind("</article")
articles = articles[:last]


# splitting articles into a list for processing in the upcoming loop
articleTextList = articles.split("</article>")
articleObjects = []

for workingArticle in articleTextList:
    currentArticle = Article(classifierWords, workingArticle)
    articleObjects.append(currentArticle)

finalCsv = makeCsv(articleObjects)

with open("csvData.txt","w") as f:
    f.write(finalCsv)




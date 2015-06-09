from __future__ import division
import re


LOWEST_GRADE = 1
HIGHEST_GRADE = 5
MAX_WORD_COUNT = 20


class Article(object):
    def __init__(self, keywords, article_text):
        self.keywords = keywords
        self.article_text = article_text.replace("  ", "")
        self.keywordFrequencies = []
        self.score = 0.0

        for word in keywords:
            regex = "[ \.\?\"\'!,]" + word + "[ \.\?\"\'!,s]"
            count = len(re.findall(regex, self.article_text.lower()))
            normalized_score = count / MAX_WORD_COUNT
            self.keywordFrequencies.append(normalized_score)

    def get_text(self):
        return self.article_text

    def get_score(self):
        return self.score

    def set_score(self, score_value):
        self.score = score_value

    def get_data(self):
        return self.keywordFrequencies


    def report(self):
        csv = ""
        for value in self.keywordFrequencies:
            csv = csv + str(value) + ","
        csv = csv + str(self.score) + "\n"

        return csv


def score_articles(article_object_list):
    counter = 0
    scored_articles = []

    for articleOb in article_object_list:

        current = articleOb.get_text()

        while len(current) > 0:
            # prints out one line for the user to read
            try:
                print(current[:70])
            except UnicodeEncodeError:
                pass

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

        # Normalizing the data on the scale of zero to one
        grade = (int(grade) - LOWEST_GRADE) / (HIGHEST_GRADE - LOWEST_GRADE)

        articleOb.set_score(grade)
        scored_articles.append(articleOb)

        finished = input("Done?(y/n)\n")

        if finished == "y":
            return scored_articles

    return scored_articles





if __name__ == "__main__":
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
    articleTextList = articles.split("</article>")
    articleObjects = []

    for workingArticle in articleTextList:
        currentArticle = Article(classifierWords, workingArticle)
        articleObjects.append(currentArticle)

    graded_articles = score_articles(articleObjects)

    print("Writing csv to file csvData.csv")
    with open("csvData.csv", "w") as f:
        for a in graded_articles:
            f.write(a.report())




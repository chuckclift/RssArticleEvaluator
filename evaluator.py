#!/usr/bin/python

import pickle
import re

def print_article(article_text):
    counter = 0
    word_list = article_text.split()

    while len(word_list) > 0:

        # generating the line of text for reading 
        line = ""
        while len(line) < 70:
            # if the word list is empty, the article is 
            # finished, so the loop can be broken out of
            if len(word_list) == 0:
                break

            # adding new word to line because there is enough room
            if len(line) + len(word_list[0]) < 70:
                line = line + " " + word_list[0]
                word_list = word_list[1:]

            # otherwise, the word would put the line length
            # over 70 characters, so this line is as big as
            # it can be
            else:
                break

            
        # prints out one line for the user to read
        try:
            print(line)
        except UnicodeEncodeError:
            pass


        # every fifth line, it stops
        # and waits for the user to read
        counter += 1
        if counter >  5:
            counter = 0
            _ = input(" ")
            # user presses enter to continue reading


def ask_for_category(category_list):
    grade = ""
    while len(grade) ==  0:
        print("Pick a category that describes this article.")
        print("\n".join(category_list) + "\n")
        grade = input("category: ")

        if len(grade) == 0:
            print("\n")
        elif grade not in category_list:
            grade = ""
            print("invalid category")
      
    return grade
   
def main():
    with open("content.txt") as g:
        articles = g.read()

    with open("categories.txt") as c:
        grading_categories = c.read().split("\n")
        grading_categories = [a.strip() for a in grading_categories]
        grading_categories = [a for a in grading_categories if len(a) > 0]

    # normalizing the whitespace
    articles = articles.split()
    articles = " ".join(articles)
   
    # retreiving the article titles and content 
    titles = re.findall(r'<title>(.*?)</title>', articles)
    texts = re.findall(r'<article>(.*?)</article>', articles)

    # adding the title to the text so it can be read and evalutated
    texts = [ a + " " +  b for a, b in zip(titles, texts)]


    # forming a list of graded articles so, if the user does not finish all
    # of the articles, the list of scores and the list of articles will
    # be the same length
    graded_articles = []

    # scoring each article
    for grading_text, grading_title in zip(texts, titles):
        print_article(grading_text)

        # these are here so the user knows the grading prompt 
        # is about to come up 
        input("")
        input("")
        input("")
     
        category = ask_for_category(grading_categories)

        graded_articles.append((grading_title, category, grading_text))

        finished = input("Done?(y/n)\n")
        if finished == "y":
            break
   

    with open("gradedArticles.pkl", "wb") as a:
        pickle.dump(graded_articles, a) 
        print("Wrote info to gradedArticles.pkl")




if __name__ == "__main__":
    main()

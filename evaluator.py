# coding: utf-8
import time
import re

commonWords = open("commonWords.txt").read().split("\n")
commonWords = [word.strip() for word in commonWords]

articles = open("articles.txt").read()


##cleans up the formatting, making it
##more readable
articles = articles.replace("<article>","")
articles = articles.replace("   ","")
articles = articles.replace("\n"," ")

##getting rid of the space after the last
##article
last = articles.rfind("</article")
articles = articles[:last]


##splitting articles into a list for processing
##in the upcoming loop
articles = articles.split("</article>")


for workingArticle in articles:
    modifiedArticle = workingArticle.lower()
    unwantedChars = ("," , "?" , "!" , "."  , "/" , "(" , ")" , ":")

    for char in unwantedChars:
        modifiedArticle = modifiedArticle.replace(char, " ")               
                
    wordList = modifiedArticle.split(" ")
    wordList = [word.strip() for word in wordList]
    
    wordList = filter(None, wordList) ##removes all empty strings
    wordList = [word for word in wordList]  ##converting it back into a list

    for i in commonWords:
        while wordList.count(i) > 0:
            wordList.pop(wordList.index(i))
        
    
    for word in wordList:
        print(word)

        



counter =0
gradeList = []
finalCsv = ""


for current in articles:
    articleLength = len(current)
  

    

    while len(current) > 0:
        ##prints out one line for the user to read
        print(current[:70])
        current = current[70:]


        ##every fifth line, it stops
        ##and waits for the user to read
        counter += 1
        if counter is 5:
            counter = 0
            var = input("")
            ##user presses enter to continue reading

    ##after the user is done reading, he is asked
    ##to assign a grade.  It won't let him submit
    ##an empty string so he doesn't accidentally
    ##skip this part
    grade = ""
    #if articleLength > 0:      ##this skips any empty articles that might
    while len(grade) is 0:
        grade = input("Grade??(1-10)")
    gradeList.append(grade)
        

for grade in gradeList:
    print(grade)







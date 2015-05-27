# coding: utf-8
import time


## includes the word with spaces and punctuation
## to ensure that we aren't counting when the word
## is inside of another word

## for each word add to search terms
## " " + word + " "
## " " + word + "\."


keywords = []
newKeyword = ""

while len(newKeyword) ==0:
    newKeyword = input("Enter a keyword \n")
    if newKeyword == "done":
        break
    keywords.append(newKeyword)
    newKeyword = ""

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

counter =0
gradeList = []
finalCsv = ""

for current in articles:
    articleLength = len(current)

    for i in keywords:
        regex = "[., ]" + i + "[., ]"
        count = len(re.findall(regex, current))
        finalCsv = finalCsv + count
    

    

    while len(current) > 0:
        ##prints out one line for the user to read
        print(current[:70])
        current = current[70:]


        ##every fifth line, it stops
        ##and waits for the user to read
        counter += 1
        if counter == 5:
            counter = 0
            var = input("")
            ##user presses enter to continue reading

    ##after the user is done reading, he is asked
    ##to assign a grade.  It won't let him submit
    ##an empty string so he doesn't accidentally
    ##skip this part
    grade = ""
    #if articleLength > 0:      ##this skips any empty articles that might
    while len(grade) == 0:
        grade = input("Grade??(1-10)")
    gradeList.append(grade)
        

for grade in gradeList:
    print(grade)







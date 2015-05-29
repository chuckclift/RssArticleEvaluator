import time
import re

classifierFile = open("classifierWords.txt", encoding="utf8")
classifierWords = classifierFile.read()
classifierWords = classifierWords.split("\n")
classifierWords = filter(None, classifierWords)
classifierWords = [word.strip() for word in classifierWords]
classifierFile.close()


articleFile = open("articles.txt", encoding="utf8")
articles = articleFile.read()
articleFile.close()

class Article(object):
    


    def __init__(self, searchKeywords, thisArticleText):
        self.searchKeywords = searchKeywords
        self.articleText = thisArticleText.replace("  ", "")
        self.keywordFrequencies = []

        for word in searchKeywords:
            count = 0
            regex = "[ \.\?\"\'!,]" + word + "[ \.\?\"\'!,s]"
            count = len(re.findall(regex, self.articleText))
            self.keywordFrequencies.append(count)
            



    def getText(self):
        return self.articleText

    def reportData(self):
        csv = ""
        for value in self.keywordFrequencies:
            csv = csv + str(value) + ","
            
        return csv

        


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
articleTextList = articles.split("</article>")
articleObjects = []


for workingArticle in articleTextList:
    current = Article(classifierWords, workingArticle)
    articleObjects.append(current)



counter =0
gradeList = []
finalCsv = ""


for articleOb in articleObjects:

    current = articleOb.getText()
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
    ##to assign a category.  It won't let him submit
    ##an empty string so he doesn't accidentally
    ##skip this part
    category = ""
    while len(category) is 0:
        category = input("Category??(product, news, linux)")
    finalCsv = finalCsv + articleOb.reportData() + category + "\n"
        

print(finalCsv)





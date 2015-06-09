# RssArticleEvaluator




This is a small project for the purpose of generating inputs for a machine learning program and applying those inputs to score articles from rss feeds.  
The program prints out the article a few lines at a time, and at the end of the article, it 
prompts the user for some sort of evaluation.  Currently, it prompts the user for a number,
but this could be tweaked to ask the user for the purpose of clustering the article. 
  It will take statistics of the number of occurences of important words (it will decide which ones are important based on the words in classifierWords.txt) and it will output this data into a .csv file.  This can then be used by the autograder to grade future articles.
  

future work:
    use a more general approach to keywords (perhaps replacing keywords with a scikit learn function)
    ex: see http://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html#extracting-features-from-text-files


This is a personal project, so feel free to use this code however you want to.

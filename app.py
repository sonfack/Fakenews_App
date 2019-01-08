from flask import Flask, render_template, request, redirect, url_for
from newspaper import Article
import os, pickle

from src.bagOfWords import bagOfWords
from src.googleSearch import readUrlFromGoogleSearch, google_search

app = Flask(__name__)
app.debug = True

def getArtcle(url):
    article = Article(url)
    article.download()
    article.parse()
    content = article.text
    article.nlp()
    keywords = article.keywords
    return content, keywords




"""
    test url ;
    https://www.bbc.com/news/world-us-canada-46754048

"""

def testModelWithText(content, modelfile):
    corpus = []
    #print(content)

    # create corpus
    corpus.append(content)

    # load model and vocabulary
    folder = "./models"
    filepath = os.path.join(folder, modelfile)
    pickle_off = open(filepath, "rb")
    model = pickle.load(pickle_off)
    clf = model['modle']
    vocabulary = model['vocabulary']

    # create test data
    X = bagOfWords(corpus, vocabulary)
    print(clf.predict_proba(X))
    return clf.predict(X), clf.predict_proba(X)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/url', methods=['POST', 'GET'])
def getUrl():
    #import pdb; pdb.set_trace()
    url = request.form['inputUrl']
    content, keywords = getArtcle(url)
    listUril = readUrlFromGoogleSearch(google_search('+'.join(keywords)))
    count = 0
    for url in listUril:
        cont , key = getArtcle(url)
        t, p = testModelWithText(cont, "modelLRVocab" )
        print("url :",url)
        print("test :",t)
        print(" proba :", p)
        if t == 1:
            count = count + 1

    if count > len(listUril)//2:
        test2 = "vrai   :"+str(count)+'/'+str(len(listUril))
    else:
        test2 = "faux   :"+str(len(listUril)-count)+'/'+str(len(listUril))
    print("#########################################################################################################")
    test, probability = testModelWithText(content, "modelLRVocab")
    print(test)
    return render_template("index.html", test=test, probability=probability, test2=test2)

@app.route('/administrator')
def admin():
    return  "Admininstrion interface"

if __name__ == '__main__':
    app.run()
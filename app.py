from flask import Flask, render_template, request, redirect, url_for
from newspaper import Article
import os, pickle

from src.bagOfWords import bagOfWords

app = Flask(__name__)
app.debug = True

def getArtcle(url):
    article = Article(url)
    article.download()
    article.parse()
    content = article.text
    return content

"""
    test url ;
    https://www.bbc.com/news/world-us-canada-46754048

"""

def testModelWithText(content, modelfile):
    corpus = []
    print(content)

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


@app.route('/url', methods=['POST'])
def getUrl():
    #import pdb; pdb.set_trace()
    url = request.form['inputUrl']
    content = getArtcle(url)
    test, probability = testModelWithText(content, "modelLRVocab")
    print(test)
    return render_template("index.html", test=test, probability=probability)

@app.route('/administrator')
def admin():
    return  "Admininstrion interface"

if __name__ == '__main__':
    app.run()
import sklearn
from sklearn.feature_extraction.text import CountVectorizer
import scipy
'''
corpus = [
'All my cats in a row',
'When my cat sits down, she looks like a Furby toy!',
'The cat from outer space',
'Sunshine loves to sit like this for some reason.'
]
'''
def bagOfWords(corpus, vocabulary):
    vectorizer = CountVectorizer()
    vectorizer.fit_transform(vocabulary)
    return vectorizer.transform(corpus).todense()
    #vectorizer = sklearn.feature_extraction.text.CountVectorizer(vocabulary)
    #return vectorizer.fit_transform(corpus).todense()

#print(bagOfWords(corpus))
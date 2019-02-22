from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.preprocessing import normalize
import pandas as pd
import numpy as np
from textblob import TextBlob
import nltk
class FeatureExtraction:
    def __init__(self,list):
        self.list = []
        self.list = list
        self.TFIDFList = []
        self.SentimentList = []
        self.SubjList = []
    def tfidf(self):
        index = 0
        for Text in self.list:
            corpus = {index:Text}
            cvect = CountVectorizer(ngram_range=(1, 1), token_pattern='(?u)\\b\\w+\\b')
            try:
                counts = cvect.fit_transform(corpus.values())
                normalized_counts = normalize(counts, norm='l1', axis=1)
                tfidf = TfidfVectorizer(ngram_range=(1, 1), token_pattern='(?u)\\b\\w+\\b', smooth_idf=False)
                tfs = tfidf.fit_transform(corpus.values())
                new_tfs = normalized_counts.multiply(tfidf.idf_)
                feature_names = tfidf.get_feature_names()
                corpus_index = [n for n in corpus]
                df = pd.DataFrame(new_tfs.T.todense(), index=feature_names, columns=corpus_index)
                T = new_tfs.toarray()
                self.TFIDFList.append(T)
            except:
                x = np.array([[0.0], [0.0]], np.float32)
                self.TFIDFList.append(x)
            index = index+1
        return self.TFIDFList
    def Sentiment(self):
        for x in range(len(self.list)):
            polartiy = TextBlob(self.list[x]).sentiment
            self.SentimentList.append(polartiy.polarity)
            self.SubjList.append(polartiy.subjectivity)
        return self.SentimentList, self.SubjList
    def TFIDF(self):
        cvect = CountVectorizer(ngram_range=(1, 1), token_pattern='(?u)\\b\\w+\\b')
        counts = cvect.fit_transform(self.list)
        normalized_counts = normalize(counts, norm='l1', axis=1)
        tfidf = TfidfVectorizer(ngram_range=(1, 1), token_pattern='(?u)\\b\\w+\\b', smooth_idf=False)
        tfs = tfidf.fit_transform(self.list)
        new_tfs = normalized_counts.multiply(tfidf.idf_)
        feature_names = tfidf.get_feature_names()
        corpus_index = [n for n in self.list]
        df = pd.DataFrame(new_tfs.T.todense(), index=feature_names, columns=corpus_index)
        T = new_tfs.toarray()
        return T


    # def CountVec(self):
    #
    #     self.ProcessedList = []
    #     for ListItem in self.list:
    #         if (len(ListItem) > 0):
    #             self.ProcessedList.append(nltk.word_tokenize(ListItem))
    #     vectorizer = CountVectorizer()
    #     x = 0
    #     for z in self.ProcessedList:
    #         print(x)
    #         x = x+1
    #         try:
    #             vectorizer.fit(z)
    #         except:
    #             print("Bad")
    #     x = vectorizer.transform(self.list).toarray()
    #     return x

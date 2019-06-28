from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.preprocessing import normalize
import pandas as pd
import numpy as np
class FeatureExtraction:
    def __init__(self,list):
        print("Feature Extraction Started")
        self.list = []
        self.list = list
        self.TFIDFList = []
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
        print("Feature Extraction Finished")
        return self.TFIDFList
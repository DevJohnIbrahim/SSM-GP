from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.preprocessing import normalize
import pandas as pd
class FeatureExtraction:
    def __init__(self,list):
        self.list = [[]]
        self.list = list
    def tfidf(self):
        print("Feature Extraction")
        for i in range(len(self.list)):
            Text = ""
            for j in range(len(self.list[i])):
                Text = Text+" "+self.list[i][j]
            corpus = {1:Text}
            cvect = CountVectorizer(ngram_range=(1, 1), token_pattern='(?u)\\b\\w+\\b')
            counts = cvect.fit_transform(corpus.values())
            normalized_counts = normalize(counts, norm='l1', axis=1)
            tfidf = TfidfVectorizer(ngram_range=(1, 1), token_pattern='(?u)\\b\\w+\\b', smooth_idf=False)
            tfs = tfidf.fit_transform(corpus.values())
            new_tfs = normalized_counts.multiply(tfidf.idf_)
            feature_names = tfidf.get_feature_names()
            corpus_index = [n for n in corpus]
            df = pd.DataFrame(new_tfs.T.todense(), index=feature_names, columns=corpus_index)
            T = [feature_names, new_tfs.todense()]
            print(T)
import sys, json, numpy as np
import firebase_admin
from PreProcessing import Pre_Processing
import pandas as pd
from FeatureExtraction import FeatureExtraction
from Processing import Processing
from firebase_admin import firestore , credentials
import nltk

def bagOfWords (message):
    sentences = nltk.word_tokenize (message)
    numofwords=sentences.__len__()

    data = pd.read_csv('bad-words.csv', encoding='ISO-8859-1')
    for x in range(1616):
        for j in range(numofwords):
            if data.values[x]==sentences[j]:
                return 1
    return 0

def read_in():
    lines = sys.stdin.readlines()
    return json.loads(lines[0])

def main():
    lines = read_in()
    np_lines = np.array(lines)
    lines = list(np_lines)
    Message = lines[0]
    From = lines[1]
    Time = lines[2]
    ChatID = lines[3]
    Answers = []
    Answers.append(Message)
    PreProcessing = Pre_Processing(Answers)
    Answers = PreProcessing.MainFunction()
    del Answers[0]
    Features = FeatureExtraction(Answers)
    Answers = Features.Test_TFIDF()
    Data1 = pd.DataFrame(Answers)
    del Answers
    Data1 = Data1.fillna(0)
    SentimentList = Features.Sentiment()
    Data1[315477] = SentimentList
    Processing_Object = Processing(Data1)
    Results = Processing_Object.Testing()


    Classified = db.collection(u"Chat").document(ChatID).collection(u"chating")
    Classified.add({
        u"message": Message,
        u"from": From,
        u"time": Time,
        u"Class": str(Results[0])
    })
    print ("Message Has Been Classified")

if __name__ == '__main__':
    cred = credentials.Certificate("AdminSDK.json")
    firebase_admin.initialize_app(cred)

    db = firestore.client()

    main()
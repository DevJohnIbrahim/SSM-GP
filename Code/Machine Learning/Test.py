import time
import _thread
import os
import sys
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

def Classification(Data , ID ):
    Answers = []
    Message = Data['message']
    Answers.append(Data['message'])
    Result = bagOfWords(Message)
    if Result == 1:
        PreProcessing = Pre_Processing(Answers)
        Answers = PreProcessing.MainFunction()
        del Answers[0]
        Features = FeatureExtraction(Answers)
        Answers = Features.Test_TFIDF()
        print(Answers.shape)
        print("Finished TF-IDF Training")
        Data1 = pd.DataFrame(Answers)
        del Answers
        Data1 = Data1.fillna(0)
        SentimentList = Features.Sentiment()
        Data1[315477] = SentimentList
        Processing_Object  = Processing(Data1)
        Results = Processing_Object.Testing()
    else:
        Results = []
        Results.append(0)
    print("Finished Classification")
    Message = Data['message']
    From = Data['from']
    Time = Data['time']
    ChatID  = Data['ChatID']
    Classified = db.collection(u"Chat").document(ChatID).collection(u"chating").document()
    Classified.set({
        u"message":u""+Message,
        u"from": u""+From,
        u"time": u""+Time,
        u"Class": u""+str(Results[0])
    })
    db.collection("NeedClassification").document(ID).delete()
    print(Classified)
    print(Results)
cred = credentials.Certificate("ssmproject-61dec-firebase-adminsdk-op5bp-d525c0a76e.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

NeedClassification = db.collection("NeedClassification")
while 1:
    docs = NeedClassification.get()
    print("Iteration")
    if docs != None:
        for doc in docs:
            print("Found Messages that need Classification")
            if doc != None:
                data = doc.to_dict()
                _thread.start_new_thread(Classification , (data , doc.id))
                db.collection("NeedClassification").document(doc.id).delete()

                doc = None
                docs = None
    time.sleep(1)


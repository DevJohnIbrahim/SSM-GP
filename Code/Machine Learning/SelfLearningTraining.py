import pandas as pd
import csv
import os
from PreProcessing import Pre_Processing
from FeatureExtraction import FeatureExtraction
from Processing import Processing
Messages = []
Labels = []
with open("NeedClassification.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        Messages.append(row[1])
        Labels.append(row[2])
del Messages[0]
del Labels[0]
Class1 = False
Class2 = False
for i in Labels:
    if i == "0":
        Class1 = True
    if i == "1":
        Class2 = True
if Class1 and Class2:
    PreProcessing = Pre_Processing(Messages)
    Answers = PreProcessing.MainFunction()
    del Answers[0]
    Features = FeatureExtraction(Answers)
    Answers = Features.Test_TFIDF()
    Data = pd.DataFrame(Answers)
    del Answers
    Data = Data.fillna(0)
    SentimentList = Features.Sentiment()
    Data[315477] = SentimentList
    Processing_Object  = Processing(Data , Labels)
    Processing_Object.Training()
    os.remove("NeedClassification.csv")
else:
    print("There should be 2 Classes to Train the Classifier Get More Data and Try again")


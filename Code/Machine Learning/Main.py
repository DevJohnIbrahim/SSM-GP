from PreProcessing import Pre_Processing
from FeatureExtraction import FeatureExtraction
from Processing import Processing
import pandas as pd

Answers = ["You are Trash" , "Take the Trash Out" , "Take the Trash" , "Eat with me", "what a stupid book"
           ,"How old are you" , "why don't you kill your self" , "You are a stupid" , "You are stupid Mohamed","I am really Sorry",
           "Please Go anywhere"]
Answers2 = Answers
PreProcessing = Pre_Processing(Answers)
Answers = PreProcessing.MainFunction()
del Answers[0]

Features = FeatureExtraction(Answers)
Answers = Features.Test_TFIDF()
Data = pd.DataFrame(Answers)
Data = Data.fillna(0)
SentimentList = Features.Sentiment()
Data[44247] = SentimentList
Processing_Object  = Processing(Data)

Results = Processing_Object.Testing()
for x in range(len(Results)):
    if Results[x] == 0:
        Result = "Not Cyberbullying"
    else:
        Result = "Cyberbullying"
    print(Answers2[x]," is:", Result)


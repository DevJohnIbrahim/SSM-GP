from FileManager import File_Manager
from DatasetFilter import Filters
from PreProcessing import Pre_Processing
from FeatureExtraction import FeatureExtraction
from Processing import Processing
import pandas as pd

FileManager_Object = File_Manager('Dataset.csv')
FileManager_Object.Read_CSV_File()
Answers = FileManager_Object.PostList
Severity = FileManager_Object.Ans1List
size = len(Severity)
x=0
while x < size:
    if Severity[x] == "No":
        Severity[x] = 0
        x = x+1
    elif Severity[x] == "Yes":
        Severity[x] = 1
        x = x+1
    else:
        del Severity[x]
        del Answers[x]
        size = size -1
DatasetFilter = Filters(Answers, Severity)
DatasetFilter.SizeFilter()
DatasetFilter.DatasetBalancing()
Answers = DatasetFilter.Answers
print(len(Answers))
Severity = DatasetFilter.Severity
PreProcessing = Pre_Processing(Answers)
Answers = PreProcessing.MainFunction()
del Answers[0]
Features = FeatureExtraction(Answers)
Answers = Features.Test_TFIDF()
print(Answers.shape)
print("Finished TF-IDF Training")
Data = pd.DataFrame(Answers)
del Answers
Data = Data.fillna(0)
SentimentList = Features.Sentiment()
Data[315477] = SentimentList
Processing_Object = Processing(Data , Severity)
Processing_Object.Training()


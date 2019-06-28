from FileManager import File_Manager
from DatasetFilter import Filters
from PreProcessing import Pre_Processing
from FeatureExtraction import FeatureExtraction
from Processing import Processing
import pandas as pd

FileManagerObject = File_Manager()
FileManagerObject.Read_CSV_File()
Answers = FileManagerObject.PostList
Severtiy = FileManagerObject.Ans1List
del Answers[0]
del Severtiy[0]
for i in range(len(Severtiy)):
    x = int(Severtiy[i])
    if x > 0:
        Severtiy[i] = 1
    else:
        Severtiy[i] = 0
print(len(Answers))
#DatasetFilter = Filters(Answers, Severtiy)
#DatasetFilter.SizeFilter()
#DatasetFilter.DatasetBalancing()
#Answers = DatasetFilter.Answers
#Severtiy = DatasetFilter.Severity
# Answers = ['Go to hell' , "You are trash" , "Take the trash out" , "idiot"]
PreProcessing = Pre_Processing(Answers)
Answers = PreProcessing.MainFunction()
del Answers[0]
FeatureExtractionObject = FeatureExtraction(Answers)
Answers = FeatureExtractionObject.Training_TFIDF()
Data = pd.DataFrame(Answers)
del Answers
SentimentList = FeatureExtractionObject.Sentiment()
print(Data.shape)
Shape = Data.shape
Data[Shape[1]] = SentimentList
del SentimentList
Processing_Object = Processing(Data, Severtiy)
Processing_Object.Training()

from FileManager import File_Manager
from DatasetFilter import Filters
from PreProcessing import Pre_Processing
from FeatureExtraction import FeatureExtraction
from Processing import Processing
import pandas as pd
import numpy as np
#Reading Dataset
# FileManager_Object = File_Manager('Dataset.csv')
# FileManager_Object.Read_CSV_File()
# del FileManager_Object.PostList[0]
# del Severity[0]
# z=0
# for chunk in pd.read_csv("Dataset.csv" ,delimiter = '\t' , chunksize = 1000):
#     print(z)
#     Data = np.asarray(chunk)
#     Severity = []
#     Answers = []
#     for i in range(len(Data)):
#         Severity.append(Data[i][0])
#         Answers.append(Data[i][1])
#     Severity = list(Severity)
#     Answers = list(Answers)
#     Size = 0
#     i = 0
#     Size = len(Severity)
#     while i < Size:
#         try:
#             if Severity[i] == "No" or Severity[i] == '0' or Severity == 0:
#                 Severity[i] = 0
#                 i = i+1
#             elif Severity[i] == "Yes" or Severity[i] == '1' or Severity == 1:
#                 Severity[i] = 1
#                 i = i+1
#             else:
#                 Severity[i] = 0
#                 i = i+1
#         except:
#             pass
#     # print(Severity)
#     if z == 0:
#         Answers.append("You are trash")
#         Answers.append("Take the Trash Out")
#         Answers.append("Fuck you bitch")
#         Answers.append("You are a dog")
#         Answers.append("Fuck you man , you are idiot")
#         Answers.append("Go and kill yourself")
#         Severity.append(1)
#         Severity.append(0)
#         Severity.append(1)
#         Severity.append(1)
#         Severity.append(1)
#         Severity.append(1)
Answers = []
Severity = []
Answers.append("Fuck you")
Severity.append(1)
Answers.append("You are idiot")
Severity.append(1)
Answers.append("Thank You  very Much")
Severity.append(0)
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
Processing_Object  = Processing(Data , Severity)
Processing_Object.Training()


from FileManager import File_Manager
from DatasetFilter import Filters
from PreProcessing import Pre_Processing
from FeatureExtraction import FeatureExtraction
from Processing import Processing
import pandas as pd
#Reading Dataset
FileManager_Object = File_Manager('Dataset.csv')
FileManager_Object.Read_CSV_File()
del FileManager_Object.AnsList[0]
del FileManager_Object.Severity1List[0]
Size = 0
for i in range(len(FileManager_Object.Severity1List)):
    if FileManager_Object.Severity1List[i] == "None":
        FileManager_Object.Severity1List[i] = 0
    elif FileManager_Object.Severity1List[i] == "n/a":
        FileManager_Object.Severity1List[i] = 0
    else:
        x = int(FileManager_Object.Severity1List[i])
        if x>0:
            FileManager_Object.Severity1List[i] = 1
        else:
            FileManager_Object.Severity1List[i] = 0
Filter = Filters(FileManager_Object.AnsList , FileManager_Object.Severity1List)
Filter.SizeFilter()
Filter.DatasetBalancing()
Answers = Filter.Answers
Severity = Filter.Severity
#Pre Processing
PreProcessing = Pre_Processing(Answers)
Answers = PreProcessing.MainFunction()
del Answers[0]


# #Feature Extraction
Features = FeatureExtraction(Answers)
Answers = Features.TFIDF()
#Answers = Features.tfidf()
# # CountVec = Features.CountVec()


#Calibrating Answers
# NewAnswers = [[]]
# for item in Answers:
#     x=item[0].tolist()
#     NewAnswers.append(item[0])
# del NewAnswers[0]
#
# Greatest=500
# for i in range(len(NewAnswers)):
#     NewAnswers[i] = NewAnswers[i].tolist()
# for i in range(len(NewAnswers)):
#     for j in range(Greatest-len(NewAnswers[i])):
#         NewAnswers[i].append(0.0)
Data = pd.DataFrame(Answers)
Data = Data.fillna(0)
# pd.concat([Data , Data2] , axis=1)
SentimentList, SubjList = Features.Sentiment()
Data[2954] = SentimentList
Data[2955] = SubjList
print(Data.shape)
Processing_Object  = Processing(Data,Severity)
Processing_Object.Processing()


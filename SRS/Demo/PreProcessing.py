import gc
import nltk
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from FileManager import File_Manager
class Pre_Processing:
    def __init__(self, FileName):
        self.FileName = FileName
    def ReadFile(self):
        FileManagerObject = File_Manager(self.FileName)
        self.List = FileManagerObject.Read_File()
        del FileManagerObject.List
        gc.collect()
        self.Tokenization()
        self.Stemming()
        self.RemoveEncoding()
        return self.ProcessedList
    def Tokenization(self):
        self.ProcessedList = [[]]
        x=0
        for ListItem in self.List:
            if (len(ListItem)>0):
                self.ProcessedList.append( nltk.word_tokenize(ListItem[0]))
                x = x+1
        del self.ProcessedList[0]
        del self.ProcessedList[1]
        del self.List
        gc.collect()
    def Stemming(self):
        Stemmer = PorterStemmer()
        for i in range(len(self.ProcessedList)):
            for j in range(len(self.ProcessedList[i])):
                self.ProcessedList[i][j] = Stemmer.stem(self.ProcessedList[i][j])

    def Lemitization(self):
        Lem = WordNetLemmatizer()
        for i in range(len(self.ProcessedList)):
            for j in range(len(self.ProcessedList[i])):
                self.ProcessedList[i][j] = Lem.lemmatize(self.ProcessedList[i][j])

    def RemoveEncoding(self):
        for i in range(len(self.ProcessedList)):
            for j in range(len(self.ProcessedList[i])):
                Word = self.ProcessedList[i][j]
                for letter in Word:
                    if ord(letter) > 127:
                        del self.ProcessedList[i][j]
                        break
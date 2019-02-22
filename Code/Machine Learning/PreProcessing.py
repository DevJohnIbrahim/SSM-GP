import gc
import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from WordCorrection import WordCorrection
class Pre_Processing:
    def __init__(self, List):
        self.List = List

    def MainFunction(self):
        self.Tokenization()
        self.RemoveStopWord()
        self.LoweringText()
        #self.WordSizeFilter()
        self.Stemming()
        self.RemoveEncoding()
        self.WordCorrection()
        return self.NewProcessedList
    def WordCorrection(self):
        WordCorrection_Object = WordCorrection()
        self.NewProcessedList = []

        for i in range(len(self.ProcessedList)):
            Text = ""
            for j in range(len(self.ProcessedList[i])):
                Text = Text+self.ProcessedList[i][j]+" "
            self.NewProcessedList.append(Text)
        del self.ProcessedList
        gc.collect()
        #for i in range(len(self.NewProcessedList)):
         #   self.NewProcessedList[i] = WordCorrection_Object.Correction(self.NewProcessedList[i])

    def Tokenization(self):
        self.ProcessedList = [[]]
        for ListItem in self.List:
            if (len(ListItem)>0):
                self.ProcessedList.append(nltk.word_tokenize(ListItem))
        del self.List
        gc.collect()

    def Stemming(self):
        Stemmer = PorterStemmer()
        for i in range(len(self.ProcessedList)):
            for j in range(len(self.ProcessedList[i])):
                self.ProcessedList[i][j] = Stemmer.stem(self.ProcessedList[i][j])
    def RemoveEncoding(self):
        for i in range(len(self.ProcessedList)):
            for j in range(len(self.ProcessedList[i])):
                Word = self.ProcessedList[i][j]
                for letter in Word:
                    if ord(letter) > 127:
                        del self.ProcessedList[i][j]
                        break
    def RemoveStopWord(self):
        Stop_Words = set(stopwords.words('english'))
        for x in range(len(self.ProcessedList)):
            size = len(self.ProcessedList[x])
            y = 0
            while y < size:
                if self.ProcessedList[x][y] in Stop_Words:
                    del self.ProcessedList[x][y]
                    size = size-1
                else:
                    y = y+1
    def LoweringText(self):
        for x in range(len(self.ProcessedList)):
            for y in range(len(self.ProcessedList[x])):
                self.ProcessedList[x][y] = self.ProcessedList[x][y].lower()
    def WordSizeFilter(self):
        for x in range(len(self.ProcessedList)):
            size = len(self.ProcessedList[x])
            y = 0
            while y < size:

                if len(self.ProcessedList[x][y]) < 3:
                    del self.ProcessedList[x][y]
                    size = size-1
                else:
                    y = y+1

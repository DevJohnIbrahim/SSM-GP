from PreProcessing import Pre_Processing
list = [[]]
Pre_Processing_Object = Pre_Processing("Dataset.csv")
list = Pre_Processing_Object.ReadFile()
for i in list:
    print(i)
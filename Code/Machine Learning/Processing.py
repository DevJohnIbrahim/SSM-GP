from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics
from joblib import dump,load
class Processing:
    def __init__(self,VectorList , ClassList):
        print("Processing Started")
        self.ClassList = ClassList
        self.VectorList = VectorList

    def Processing(self):
        X_train, X_test, y_train, y_test = train_test_split(self.VectorList, self.ClassList, test_size=0.20,random_state=100)
        clf = svm.NuSVC() # Linear Kernel
        print("Training Started")
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        print("Accuracy:", metrics.accuracy_score(y_test, y_pred)*100)
        print("Recall:", metrics.recall_score(y_test, y_pred)*100)
        dump(clf , "TrainedModel.Model")





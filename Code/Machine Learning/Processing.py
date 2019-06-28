from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from joblib import dump,load
class Processing:
    def __init__(self , VectorList , ClassList = None):
        self.VectorList = VectorList
        self.ClassList = ClassList
        del VectorList
        del ClassList

    def Training(self):
        print("Processing Started")
        # X_train, X_test, y_train, y_test = train_test_split(self.VectorList, self.ClassList, test_size=0.10,random_state=100)
        # clf = linear_model.SGDClassifier(max_iter=1000, tol=1e-3, warm_start=True)
        clf = SVC(kernel="linear")
        # clf = load("TrainedModel.Model")
        # print("Training Started")
        clf.fit(self.VectorList , self.ClassList)
        # y_pred = clf.predict(X_test)
        # print("Accuracy:", metrics.accuracy_score(y_test, y_pred) * 100)
        # print("Recall:", metrics.recall_score(y_test, y_pred) * 100)
        # print("Percsion" , metrics.precision_score(y_test , y_pred) * 100)
        dump(clf, "TrainedModel.Model")

    def Testing(self):
        clf = load("TrainedModel.Model")
        y_pred = clf.predict(self.VectorList)
        return y_pred






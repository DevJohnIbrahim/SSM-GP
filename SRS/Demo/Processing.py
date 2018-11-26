from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestRegressor
import numpy as np
class Processing:
    def __init__(self,VectorList , ClassList):
        self.ClassList = ClassList
        self.VectorList = VectorList

    def Processing(self):
        print("Processing Started")
        X_train, X_test, y_train, y_test = train_test_split(self.VectorList, self.ClassList, test_size=0.20)
        print("Training Started")
        # Instantiate model with 1000 decision trees
        rf = RandomForestRegressor(n_estimators=1000, random_state=42)
        # Train the model on training data
        rf.fit(X_train, y_train);

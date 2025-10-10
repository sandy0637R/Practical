import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

def importdata():
    col_names = ['Class', 'Left-Weight', 'Left-Distance', 'Right-Weight', 'Right-Distance']
    balance_data = pd.read_csv("balance-scale.data", names=col_names)
    print("Dataset Length:", len(balance_data))
    print("Dataset Shape:", balance_data.shape)
    print("\nFirst 5 Records:\n", balance_data.head())
    return balance_data

def splitdataset(balance_data):
    X = balance_data.values[:, 1:5]
    Y = balance_data.values[:, 0]
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=100)
    return X, Y, X_train, X_test, y_train, y_test

def train_using_entropy(X_train, y_train):
    clf_entropy = DecisionTreeClassifier(criterion="entropy", random_state=100, max_depth=3, min_samples_leaf=5)
    clf_entropy.fit(X_train, y_train)
    return clf_entropy

def prediction(X_test, clf_object):
    y_pred = clf_object.predict(X_test)
    print("\nPredicted Values:\n", y_pred)
    return y_pred

def cal_accuracy(y_test, y_pred):
    print("\nAccuracy:", accuracy_score(y_test, y_pred) * 100, "%")
    print("\nClassification Report:\n", classification_report(y_test, y_pred))

def main():
    data = importdata()
    X, Y, X_train, X_test, y_train, y_test = splitdataset(data)
    clf_entropy = train_using_entropy(X_train, y_train)
    print("\nResults using Entropy Criterion:")
    y_pred_entropy = prediction(X_test, clf_entropy)
    cal_accuracy(y_test, y_pred_entropy)

if __name__ == "__main__":
    main()

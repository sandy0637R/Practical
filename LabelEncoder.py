import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Read dataset
iris = pd.read_csv("Iris.csv")

print(iris)

# Encode categorical column
le = LabelEncoder()
iris["code"] = le.fit_transform(iris["Species"])

print(iris)
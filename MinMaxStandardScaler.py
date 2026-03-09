import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Read dataset
df = pd.read_csv("wine.csv", usecols=["Alcohol", "Malic Acid"])

print("Original dataset")
print(df)

# ----- MinMax Scaling -----
scaler = MinMaxScaler()
scaled_values = scaler.fit_transform(df)

df[["Alcohol", "Malic Acid"]] = scaled_values

print("DataFrame after MinMax Scaling")
print(df)

# ----- Standard Scaling -----
scaler = StandardScaler()
scaled_standard = scaler.fit_transform(df)

df[["Alcohol", "Malic Acid"]] = scaled_standard

print("DataFrame after Standard Scaling")
print(df)
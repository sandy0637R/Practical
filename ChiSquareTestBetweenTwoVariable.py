import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import warnings

warnings.filterwarnings("ignore")

# Load dataset
df = sns.load_dataset("mpg")

print(df)

# Describe columns
print(df["horsepower"].describe())
print(df["model_year"].describe())

# Binning horsepower
bins_hp = [0, 75, 150, 240]
labels_hp = ["low", "medium", "high"]

df["horsepower_new"] = pd.cut(df["horsepower"], bins=bins_hp, labels=labels_hp)

print(df["horsepower_new"])

# Binning model year
bins_year = [69, 72, 75, 84]
labels_year = ["old", "mid", "new"]

df["modelyear_new"] = pd.cut(df["model_year"], bins=bins_year, labels=labels_year)

print(df["modelyear_new"])

# Contingency table
df_chi = pd.crosstab(df["horsepower_new"], df["modelyear_new"])

print(df_chi)

# Chi-square test
print(stats.chi2_contingency(df_chi))
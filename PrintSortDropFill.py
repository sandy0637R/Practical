#Read Dataset
import pandas as pd

df = pd.read_csv("student.csv")

print("Dataset")
print(df)



#Remove Rows
import pandas as pd

# Read CSV file
df = pd.read_csv("titanic.csv")

print("Dataset")
print(df)

print(df.head(10))

print("Dataset after dropping NA values")

# Remove rows with missing values
df.dropna(inplace=True)

print(df)


#Fill Na 
import pandas as pd

df = pd.read_csv("titanic.csv")

print(df.head())

print("Dataset after filling NA values with 0")

df2 = df.fillna(value=0)

print(df2)



#Iris 
import pandas as pd

iris = pd.read_csv("Iris.csv")

# Filter setosa samples
setosa = iris[iris['species'] == 'setosa']

print("Setosa samples:")
print(setosa.head())

# Sort dataset
sorted_iris = iris.sort_values(by="sepal_length", ascending=False)

print("Sorted Iris dataset:")
print(sorted_iris.head())

# Group by species and calculate mean
grouped_species = iris.groupby("species").mean()

print("Mean measurements of each species:")
print(grouped_species)



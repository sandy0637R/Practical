import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Read dataset
data = pd.read_csv("Wholesale customers data.csv")

# Categorical and continuous features
categorical_features = ['Channel', 'Region']
continuous_features = ['Fresh', 'Milk', 'Grocery', 'Frozen',
                       'Detergents_Paper', 'Delicassen']

# Convert categorical to dummy variables
for col in categorical_features:
    dummies = pd.get_dummies(data[col], prefix=col)
    data = pd.concat([data, dummies], axis=1)
    data.drop(col, axis=1, inplace=True)

# Scaling
mms = MinMaxScaler()
data_transformed = mms.fit_transform(data)

# Elbow Method
sum_of_squared_distances = []
K = range(1, 16)

for k in K:
    km = KMeans(n_clusters=k, random_state=42)
    km.fit(data_transformed)
    sum_of_squared_distances.append(km.inertia_)

# Plot
plt.plot(K, sum_of_squared_distances, 'bx-')
plt.xlabel("k")
plt.ylabel("Sum of Squared Distances")
plt.title("Elbow Method for Optimal k")
plt.show()
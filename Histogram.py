import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

np.random.seed(42)

# Generate samples
sample1 = np.random.normal(loc=10, scale=2, size=20)
sample2 = np.random.normal(loc=12, scale=2, size=20)

# Two sample t-test
t_statistic, p_value = stats.ttest_ind(sample1, sample2)

alpha = 0.05

print("Results of Two Sample t-test")
print("t-statistic:", t_statistic)
print("p-value:", p_value)
print("Degrees of freedom:", len(sample1) + len(sample2) - 2)

# Plot histogram
plt.figure(figsize=(10,6))

plt.hist(sample1, alpha=0.5, label="Sample 1")
plt.hist(sample2, alpha=0.5, label="Sample 2")

plt.axvline(np.mean(sample1), linestyle="dashed", linewidth=2)
plt.axvline(np.mean(sample2), linestyle="dashed", linewidth=2)

plt.title("Distribution of Sample 1 and Sample 2")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.legend()

plt.show()
import scipy.stats as stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Groups data
group1 = [23, 25, 29, 34, 20]
group2 = [19, 20, 22, 24, 25]
group3 = [15, 18, 20, 21, 17]
group4 = [28, 24, 26, 30, 29]

# One-way ANOVA
f_statistic, p_value = stats.f_oneway(group1, group2, group3, group4)

print("One-way ANOVA")
print("F-statistic:", f_statistic)
print("p-value:", p_value)

# Combine data
all_data = group1 + group2 + group3 + group4

# Labels
group_labels = (["Group1"] * len(group1) +
                ["Group2"] * len(group2) +
                ["Group3"] * len(group3) +
                ["Group4"] * len(group4))

# Tukey HSD test
tukey_results = pairwise_tukeyhsd(all_data, group_labels)

print("\nTukey HSD Post-hoc Test:")
print(tukey_results)
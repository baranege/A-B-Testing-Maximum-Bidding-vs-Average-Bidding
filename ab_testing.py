# A/B TESTING PROJCT

# Case: Firm A introduced an alternative method for bidding which is called
# average bidding for the previous method called maximum bidding.
# Firm B wants to test the outcome of this alternative method by A/B test.


import numpy as np
import pandas as pd
from scipy.stats import ttest_1samp, shapiro, levene, ttest_ind, \
    mannwhitneyu, pearsonr, spearmanr, kendalltau, f_oneway, kruskal

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 10)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

df = pd.read_excel("datasets/ab_testing.xlsx", sheet_name = "Control Group")
test_df = pd.read_excel("datasets/ab_testing.xlsx", sheet_name = "Test Group")

# Task1: Setting up the Hypothesis

# H0: There is not a difference between transformation rates,
# of the average bidding and maximum bidding.
# H1: There is a difference between transformation rates,
# of the average bidding and maximum bidding.

df.head()
test_df.head()

# Observing the average purchase
df["Purchase"].mean() #550.8940587702316
test_df["Purchase"].mean() #582.1060966484675

# Hypothesis
# H0: M1 = M2
# H1: M1 != M2

# Task 2: Testing the hypothesis

# Checking assumptions
# 1.Normality
# 2.Variance homogeneity

# 1.Normality
# H0: The data was drawn from a normal distribution
# H0: The data was not drawn from a normal distribution

test_stat, pvalue = shapiro(df["Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
# don't reject null hypothesis that the data was distributed normally


test_stat, pvalue = shapiro(test_df["Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
# don't reject null hypothesis that the data was distributed normally

# 2.Variance Homogeneity
# H0: All input samples are from populations with equal variances
# H1: They are not

test_stat, pvalue = levene(df["Purchase"], test_df["Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
# don't reject null hypothesis that input samples are from populations with equal variances

# Assumptions are valid, continue with two sample independent t-test

# Hypothesis
# H0: M1 = M2
# H1: M1 != M2

test_stat, pvalue = ttest_ind(df["Purchase"], test_df["Purchase"],
                              equal_var=True)
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
# don't reject null hypothesis, two independent samples have identical means.

# Task 3: Which test is used? Why?

# Both of the samples have been normally distributed and they have equal variances
# Proceeded with independent two sample t-test

# Task 4: Recommendations for the customer
# Average bidding and maximum bidding have identical means with 95% confidence level
# However, average bidding lead to increase in average purchase.
# Firm A can use average bidding or further analysis could be recommended.

df["Earning"].mean()
test_df["Earning"].mean()
# Here it is clearly observed that average bidding increases Firm's earnings.
# Recommendation: Keep average bidding method
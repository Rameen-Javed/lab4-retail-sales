
import pandas as pd
import numpy as np
from scipy.stats import zscore

df = pd.DataFrame({
    "Day": range(1, 11),
    "Revenue": [45, 52, np.nan, 48, 390, 55, np.nan, 50, 47, 53]
})

missing = df["Revenue"].isnull().sum()
print("Missing values in Revenue:", missing)

median_revenue = df["Revenue"].median()
df["Revenue"] = df["Revenue"].fillna(median_revenue)

print("\nAfter median fill:")
print(df)

min_val = df["Revenue"].min()
max_val = df["Revenue"].max()

df["Revenue_MinMax"] = (df["Revenue"] - min_val) / (max_val - min_val)

df["Revenue_Zscore"] = zscore(df["Revenue"])

Q1 = df["Revenue"].quantile(0.25)
Q3 = df["Revenue"].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

df["Outlier"] = (
    (df["Revenue"] < lower_bound) |
    (df["Revenue"] > upper_bound)
)

outlier_days = df.loc[df["Outlier"], "Day"].tolist()

print("\nFinal Table:")
print(df)

print("\nIQR outliers detected on day(s):", outlier_days)

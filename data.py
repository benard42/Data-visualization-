import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


# Load the data
df = pd.read_csv('data.csv')
print(df.head(5))


# Plot a histogram
sns.histplot(data=df, x='age')
plt.show()


# Plot a scatterplot
sns.scatterplot(data=df, x='area', y='price')
plt.show()

# Plot a barplot
sns.barplot(data=df, x='area', y='price')
plt.show()

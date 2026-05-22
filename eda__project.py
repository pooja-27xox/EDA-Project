import pandas as pd
import matplotlib.pyplot as plt
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
data = pd.read_csv(url)
print(data.head())
print("\nDataset Information:")
print(data.info())
print("\nStatistical Summary:")
print(data.describe())
plt.hist(data['Age'].dropna())
plt.xlabel("Age")
plt.ylabel("Number of Passengers")
plt.title("Age Distribution")
plt.show()
data['Survived'].value_counts().plot(kind='bar')
plt.xlabel("Survived")
plt.ylabel("Count")
plt.title("Passenger Survival Count")
plt.show()

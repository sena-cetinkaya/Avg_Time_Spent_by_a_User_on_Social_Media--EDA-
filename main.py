# Import the libraries.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the dataset.
data = pd.read_csv("dummy_data.csv")

# DATA ANALYSIS

# Display the first few rows of the data.
print(data.head())

# Learning the size of the dataset
print(data.shape)

# Learning columns
print(data.columns)

# Data types of columns
print(data.dtypes)

# Check for missing values
print(data.isnull().sum())

# Summary statistics
print(data.describe())

# Learning the number of unique values.
cols = ["gender", "platform", "interests", "location", "demographics", "profession"]
for col in cols:
    print(data[col].value_counts())

# DATA VISUALIZATION

# Time spent on social media based on gender
sns.barplot(x="gender", y="time_spent", data=data)
plt.title("Avg. Time Spent on Gender")
plt.xlabel("Gender")
plt.ylabel("Time Spent")
plt.show()

# Time spent on social media based on platform
sns.barplot(x="platform", y="time_spent", data=data)
plt.title("Avg. Time Spent on Platform")
plt.xlabel("Platform")
plt.ylabel("Time Spent")
plt.show()

# Time spent on social media based on interests
sns.barplot(x="interests", y="time_spent", data=data)
plt.title("Avg. Time Spent on Interest")
plt.xlabel("Interest")
plt.ylabel("Time Spent")
plt.show()

# Time spent on social media based on location
sns.barplot(x="location", y="time_spent", data=data)
plt.title("Avg. Time Spent on Location")
plt.xlabel("Location")
plt.ylabel("Time Spent")
plt.show()

# Time spent on social media based on demographics
sns.barplot(x="demographics", y="time_spent", data=data)
plt.title("Avg. Time Spent on Demographic")
plt.xlabel("Demographic")
plt.ylabel("Time Spent")
plt.show()

# Time spent on social media based on profession
sns.barplot(x="profession", y="time_spent", data=data)
plt.title("Avg. Time Spent on Profession")
plt.xlabel("Profession")
plt.ylabel("Time Spent")
plt.show()

# Time spent on social media based on gender and age
sns.barplot(x="time_spent",y="age",hue="gender", data=data)
plt.title("Time spent on social media based on gender and age")
plt.xlabel("Time Spent")
plt.ylabel("Age")
plt.show()

# Time spent on social media based on gender and profession
sns.barplot(x="profession", y="time_spent",hue="gender", data=data)
plt.title("Time spent on social media based on gender and profession")
plt.xlabel("Profession.")
plt.ylabel("Time Spent")
plt.show()

# Time spent on social media based on platform and profession
sns.barplot(x="profession", y="time_spent",hue="platform", data=data)
plt.title("Time spent on social media based on platform and profession")
plt.xlabel("Profession.")
plt.ylabel("Time Spent")
plt.show()

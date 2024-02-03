#Assignment4 - Program1
#1. Data Manipulation a. Read the provided CSV file ‘data.csv’. 
#b. https://drive.google.com/drive/folders/1h8C3mLsso-R-sIOLsvoYwPLzy2fJ4IOF?usp=sharing 
#c. Show the basic statistical description about the data. 
#d. Check if the data has null values. i. Replace the null values with the mean 
#e. Select at least two columns and aggregate the data using: min, max, count, mean. 
#f. Filter the dataframe to select the rows with calories values between 500 and 1000. 
#g. Filter the dataframe to select the rows with calories values > 500 and pulse < 100. 
#h. Create a new “df_modified” dataframe that contains all the columns from df except for “Maxpulse”. 
#i. Delete the “Maxpulse” column from the main df dataframe 
#j. Convert the datatype of Calories column to int datatype. 
#k. Using pandas create a scatter plot for the two columns (Duration and Calories). Example          

#Student Name: Yamini Saraswathi Borra
#Student ID: 700748022

import pandas as pd
import matplotlib.pyplot as plt

# Step a: Read the provided CSV file
data = pd.read_csv("C:\\Users\\M1097753\\Documents\\GITHUB\\data.csv")

# Step c: Show basic statistical description
print("Basic Statistical Description:")
print(data.describe())

# Step d: Check for null values and replace with mean
print("\nNull Values Before Replacement:")
print(data.isnull().sum())

data.fillna(data.mean(), inplace=True)

print("\nNull Values After Replacement:")
print(data.isnull().sum())

# Step e: Aggregate data using min, max, count, mean for two columns
agg_columns = ['Duration', 'Calories']
agg_functions = ['min', 'max', 'count', 'mean']
print("\nAggregating Data:")
print(data[agg_columns].agg(agg_functions))

# Step f: Filter dataframe for calories values between 500 and 1000
filtered_df_f = data[(data['Calories'] >= 500) & (data['Calories'] <= 1000)]
print("\nFiltered DataFrame for calories between 500 and 1000:")
print(filtered_df_f)

# Step g: Filter dataframe for calories > 500 and pulse < 100
filtered_df_g = data[(data['Calories'] > 500) & (data['Pulse'] < 100)]
print("\nFiltered DataFrame for calories > 500 and pulse < 100:")
print(filtered_df_g)

# Step h: Create a new dataframe df_modified without "Maxpulse"
df_modified = data.drop(columns=['Maxpulse'])
print("\nDataFrame df_modified:")
print(df_modified)

# Step i: Delete "Maxpulse" column from the main dataframe
data.drop(columns=['Maxpulse'], inplace=True)

# Step j: Convert datatype of Calories column to int
data['Calories'] = data['Calories'].astype(int)

# Step k: Scatter plot for Duration and Calories
data.plot.scatter(x='Duration', y='Calories', title='Scatter Plot: Duration vs Calories')
plt.show()

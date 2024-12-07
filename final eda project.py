# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 18:14:56 2024

@author: YELLATURU TEJASWINI
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv(r"C:\Users\YELLATURU TEJASWINI\OneDrive\Desktop\project customer segmentation\project_data (1).csv")
print(df)


#understand the data

#top five rows
df.head()

#bottom five rows()
df.tail()

# summary statistics
df.describe()

#  finding no of rows and columns 
df.shape

#data info
df.info()

#data types for each column
df.dtypes

#column names
df.columns

# find the number of unique values
df.nunique()
df['Gender'].unique()
df['Bet_Type_Preference'].unique()
df['customer_id'].unique()
df['country'].unique()
df['Age'].unique()

# cleaning the data
df.isnull().sum()

# count the missing values
null_counts=df.isnull().sum()
print(null_counts)

# drop columns with any missing values
df_cleaned = df.dropna()
print(df_cleaned)


#statistical summary of age
age_mean=df['Age'].mean()
age_median=df['Age'].median()
age_mode=df['Age'].mode()
age_max=df['Age'].max()
age_min=df['Age'].min()
age_range=df['Age'].max()-df['Age'].min()
age_var=df['Age'].var()
age_stdev=df['Age'].std()
print('avg age: ',age_mean)
print('median: ',age_median)
print('repeated_age:',age_mode)
print("max value: ",age_max)
print("min value: ",age_min)
print('range:',age_range)
print('variance : ',age_var)
print('Standard_deviation : ',age_stdev)


avg_salary=df['Salary'].mean()
median_salary=df['Salary'].median()
mode_salary=df['Salary'].mode()
max_salary=df['Salary'].max()
min_salary=df['Salary'].min()
range_salary=df['Salary'].max()-df['Age'].min()
var_salary=df['Salary'].var()
std_salary=df['Salary'].std()
print("avg_salary: ",avg_salary)
print("median: ",median_salary)
print("mode: ", mode_salary)
print("max salary: ",max_salary)
print("min salary: ",min_salary)
print("range: ", range_salary)
print("var_salary: ",var_salary)
print("std_salary: ",std_salary)

Avg_Total_Amount_Wagered=df['Total_Amount_Wagered'] .mean()
med_Total_Amount_Wagered =df['Total_Amount_Wagered'].median()
mode_Total_Amount_Wagered =df['Total_Amount_Wagered'].mode()
max_Total_Amount_Wagered =df['Total_Amount_Wagered'].max()
min_Total_Amount_Wagered =df['Total_Amount_Wagered'].min()
Range_Total_Amount_Wagered =df['Total_Amount_Wagered'].max()-df['Total_Amount_Wagered'].min()
var_Total_Amount_Wagered =df['Total_Amount_Wagered'].var()
stdev_Total_Amount_Wagered =df['Total_Amount_Wagered'].std()
print("avg Total_Amount_Wagered: ",Avg_Total_Amount_Wagered )
print("median Total_Amount_Wagered: ",med_Total_Amount_Wagered )
print("Mode Total_Amount_Wagered: ",mode_Total_Amount_Wagered )
print("Max Total_Amount_Wagered: ",max_Total_Amount_Wagered )
print("Min Total_Amount_Wagered: ",min_Total_Amount_Wagered )
print("Range Total_Amount_Wagered : ",Range_Total_Amount_Wagered)
print("var Total_Amount_Wagered: ",var_Total_Amount_Wagered )
print("stdev Total_Amount_Wagered : ",stdev_Total_Amount_Wagered)



Avg_Tno_of_Bets=df['Total_Number_of_Bets'].mean()
med_Tno_of_Bets=df['Total_Number_of_Bets'].median()
mode_Tno_of_Bets=df['Total_Number_of_Bets'].mode()
max_Tno_of_Bets=df['Total_Number_of_Bets'].max()
min_Tno_of_Bets=df['Total_Number_of_Bets'].min()
Range_Tno_of_Bets=df['Total_Number_of_Bets'].max()-df['Total_Number_of_Bets'].min()
var_Tno_of_Bets=df['Total_Number_of_Bets'].var()
stdev_Tno_of_Bets=df['Total_Number_of_Bets'].std()
print('Avg Total_Number_of_Bets: ',Avg_Tno_of_Bets)
print('med_Total_Number_of_Bets: ',med_Tno_of_Bets)
print('mode Total_Number_of_Bets: ',mode_Tno_of_Bets)
print('max Total_Number_of_Bets: ',max_Tno_of_Bets)
print('min Total_Number_of_Bets: ',min_Tno_of_Bets)
print('Range Total_Number_of_Bets: ',Range_Tno_of_Bets)
print('var Total_Number_of_Bets: ',var_Tno_of_Bets)
print('stdev Total_Number_of_Bets: ',stdev_Tno_of_Bets)


Avg_No_Bonuses_Received=df['Number_of_Bonuses_Received'].mean()
median_No_Bonuses_Received=df['Number_of_Bonuses_Received'].median()
mode_No_Bonuses_Received=df['Number_of_Bonuses_Received'].mode()
max_No_Bonuses_Received=df['Number_of_Bonuses_Received'].max()
min_No_Bonuses_Received=df['Number_of_Bonuses_Received'].min()
range_No_Bonuses_Received=df['Number_of_Bonuses_Received'].max()-df['Number_of_Bonuses_Received'].min()
var_No_Bonuses_Received=df['Number_of_Bonuses_Received'].var()
stadev_No_Bonuses_Received=df['Number_of_Bonuses_Received'].std()
print('Avg Number of Bonuses Received: ',Avg_No_Bonuses_Received)
print('median Number of Bonuses Received: ',median_No_Bonuses_Received)
print('mode number of Bonuses Received: ',mode_No_Bonuses_Received)
print('max number of Bonuses Received: ',max_No_Bonuses_Received)
print('min number of Bonuses Received: ',min_No_Bonuses_Received)
print('Range number of Bonuses Received: ',range_No_Bonuses_Received)  
print('variance Number of Bonuses Received: ',var_No_Bonuses_Received)
print('Standard deviation Number of Bonuses Received: ',stadev_No_Bonuses_Received)                                                                                                                             


Avg_Amount_of_Bonuses_Received=df['Average_Amount_of_Bonuses_Received'].mean()
med_Amount_of_Bonuses_Received=df['Average_Amount_of_Bonuses_Received'].median()
mode_Amount_of_Bonuses_Received=df['Average_Amount_of_Bonuses_Received'].mode()
max_Amount_of_Bonuses_Received=df['Average_Amount_of_Bonuses_Received'].max()
min_Amount_of_Bonuses_Received=df['Average_Amount_of_Bonuses_Received'].min()
range_Amount_of_Bonuses_Received=df['Average_Amount_of_Bonuses_Received'].max()-df['Average_Amount_of_Bonuses_Received'].min()
var_Amount_of_Bonuses_Received=df['Average_Amount_of_Bonuses_Received'].var()
stdev_Amount_of_Bonuses_Received=df['Average_Amount_of_Bonuses_Received'].std()
print('Avg_Amount_of_Bonuses_Received: ',Avg_Amount_of_Bonuses_Received)
print('med_Amount_of_Bonuses_Received: ',med_Amount_of_Bonuses_Received)
print('mode_Amount_of_Bonuses_Received: ',mode_Amount_of_Bonuses_Received)
print('max_Amount_of_Bonuses_Received: ',max_Amount_of_Bonuses_Received)
print('min_Amount_of_Bonuses_Received: ',min_Amount_of_Bonuses_Received)
print('var_Amount_of_Bonuses_Received: ',var_Amount_of_Bonuses_Received)
print('stdev_Amount_of_Bonuses_Received: ',stdev_Amount_of_Bonuses_Received)



#relationship analysis

#select only numeric columns
numeric_df=df.select_dtypes(include=['number'])
numeric_df

#corelaton matrix
correlation_matrix=numeric_df.corr()
print(correlation_matrix)

#heatmap using correlation
sns.heatmap(correlation_matrix,xticklabels=correlation_matrix.columns,yticklabels=correlation_matrix.columns,annot=True)
sns.pairplot(df)
sns.relplot(x='country',y='Age',hue='Gender',data=df)



# skewness for all numerical columns
skew_age=df['Age'].skew()
skew_age

skew_salary=df['Salary'].skew()
skew_salary

skew_Average_Amount_of_Bonuses_Received=df['Average_Amount_of_Bonuses_Received'].skew()
skew_Average_Amount_of_Bonuses_Received

skew_no_of_bonuses_received=df['Number_of_Bonuses_Received'].skew()
skew_no_of_bonuses_received

skew_tot_no_of_bets=df['Total_Number_of_Bets'].skew()
skew_tot_no_of_bets

skew_Total_Amount_Wagered=df['Total_Amount_Wagered'].skew()
skew_Total_Amount_Wagered


#kurtosis for all numeric columns
kurt_age=df['Age'].kurtosis()
kurt_age

kurt_salary=df['Salary'].kurtosis()
kurt_salary

kurt_total_no_of_bets=df['Total_Number_of_Bets'].kurtosis()
kurt_total_no_of_bets

kurt_tot_amount_wagered=df['Total_Amount_Wagered'].skew()
kurt_tot_amount_wagered

kurt_No_Bonuses_Received=df['Number_of_Bonuses_Received'].kurt()
kurt_No_Bonuses_Received

kurt_No_Bonuses_Received=df['Average_Amount_of_Bonuses_Received'].kurt()
kurt_No_Bonuses_Received

#IQR for all numerical columns
q1=df['Age'].quantile(0.25)
q3=df['Age'].quantile(0.75)
iqr=q3-q1
print(q1)
print(q3)
print(iqr)
# Determine outlier thresholds
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
print(lower_bound)
print(upper_bound)

#IQR for all numerical columns
q1=df['Salary'].quantile(0.25)
q3=df['Salary'].quantile(0.75)
iqr=q3-q1
print(q1)
print(q3)
print(iqr)
# Determine outlier thresholds
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
print(lower_bound)
print(upper_bound)


#IQR for all numerical columns
q1=df['Total_Number_of_Bets'].quantile(0.25)
q3=df['Total_Number_of_Bets'].quantile(0.75)
iqr=q3-q1
print(q1)
print(q3)
print(iqr)
# Determine outlier thresholds
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
print(lower_bound)
print(upper_bound)


#IQR for all numerical columns
q1=df['Total_Amount_Wagered'].quantile(0.25)
q3=df['Total_Amount_Wagered'].quantile(0.75)
iqr=q3-q1
print(q1)
print(q3)
print(iqr)
# Determine outlier thresholds
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
print(lower_bound)
print(upper_bound)


#IQR for all numerical columns
q1=df['Number_of_Bonuses_Received'].quantile(0.25)
q3=df['Number_of_Bonuses_Received'].quantile(0.75)
iqr=q3-q1
print(q1)
print(q3)
print(iqr)
# Determine outlier thresholds
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
print(lower_bound)
print(upper_bound)

from scipy.stats import mstats

# Winsorize the data
df['Age_Winsorized'] = mstats.winsorize(df['Age'], limits=[0.2, 0.1])  # 10% from each end
print("Data After Winsorization:",df['Age_Winsorized'])
print(df)
df['Age'].fillna(df['Age'].mean(), inplace=True)
print(df)
df['Age_Winsorized'].min()
df['Age']=df['Age_Winsorized'] 
print(df['Age'])
df['Age'].min()


df['sal_Winsorized'] = mstats.winsorize(df['Salary'], limits=[0.1, 0.1])  # 10% from each end
print("Data After Winsorization:",df['sal_Winsorized'])
print(df['sal_Winsorized'])
print(df)

df['Total_Number_of_Bets_winsorised'] = mstats.winsorize(df['Total_Number_of_Bets'], limits=[0.1, 0.1])  # 10% from each end
print("Data After Winsorization: ",df['Total_Number_of_Bets_winsorised'])
print(df)


df['Total_Amount_wagered_winsorised'] = mstats.winsorize(df['Total_Amount_Wagered'], limits=[0.1, 0.1])  # 10% from each end
print("Data After Winsorization:",df['Total_Amount_wagered_winsorised'])
print(df)


df['no_of_bonuses_received_winsorised'] = mstats.winsorize(df['Number_of_Bonuses_Received'], limits=[0.1, 0.1])  # 10% from each end
print("Data After Winsorization:",df['no_of_bonuses_received_winsorised'])
print(df)

df['avg_amount_of_bonuses_received_winsorised'] = mstats.winsorize(df['Average_Amount_of_Bonuses_Received'], limits=[0.1, 0.1])  # 10% from each end
print("Data After Winsorization:",df['avg_amount_of_bonuses_received_winsorised'])
print(df)


#visualizations
# Using Seaborn to create the box plot
sns.boxplot(x='Gender', y='Age', data=df)
plt.title('Box Plot of Age by Gender (Seaborn)')
plt.figure(figsize=(12, 6))  # Set figure size
plt.show()  # Show the plot


# Using Seaborn to create the box plot
sns.boxplot(x='country', y='Age', data=df)
plt.title('Box Plot of Age by Gender (Seaborn)')
plt.figure(figsize=(12, 6))  # Set figure size
plt.show()  # Show the plot


#using Seaborn to create the scatter plot
plt.figure(figsize=(8,6))
sns.scatterplot(data=df,x='Age',y='Salary')
plt.title("Scatte plot of age  vs Salary")
plt.show()



#using Seaborn to create the scatter plot
plt.figure(figsize=(8,6))
sns.scatterplot(data=df,x='country',y='Salary')
plt.title("Scatte plot of age  vs Salary")
plt.show()


# Create a histogram
plt.figure(figsize=(8, 6))
sns.histplot(df['Age'], bins=10, kde=True)
plt.title('Histogram of Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()


# Create a histogram
plt.figure(figsize=(8, 6))
sns.histplot(df['Salary'], bins=10, kde=True)
plt.title('Histogram of Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Create a histogram
plt.figure(figsize=(8, 6))
sns.histplot(df['Salary'])
plt.title('Histogram of salary frequency ')
plt.ylabel('frequency')
plt.xlabel('salary')
plt.show()


# create the pairplot
sns.pairplot(df, hue='Gender', diag_kind='kde', markers=["o", "s"])
plt.suptitle('Pairplot of Age, salary, and gender', y=2.02)  # Title above the plot
plt.show()

#categorical plot
sns.catplot(x='Gender', y='Age', kind='box', data=df, height=5, aspect=1.2)
# Adding a title
plt.title('Box Plot of Age by Gender')
plt.ylabel('Age')
plt.show()

#barplot
sns.barplot(x='country', y='Age', data=df, palette='viridis')
# Adding titles and labels
plt.title('Average Age by Country')
plt.xlabel('Country')
plt.ylabel('Age')
plt.xticks(rotation=45)
plt.show()


# Create a scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(y='Country', x='Age', data=df, hue='Country', palette='Set2', s=100)
# Adding titles and labels
plt.title('Age Distribution by Country')
plt.xlabel('Country')
plt.ylabel('Age')
plt.xticks(rotation=45)
plt.show()


print(df.columns)
df.shape
# Create a bar plot
sns.barplot(x='country', y='Age', data=df, palette='viridis')
# Adding titles and labels
plt.title('Average Age by Country')
plt.xlabel('Country')
plt.ylabel('Age')
plt.xticks(rotation=45)
plt.show()

# Create a bar plot
sns.barplot(x='Bet_Type_Preference', y='Salary', data=df, palette='viridis')
# Adding titles and labels
plt.title('Salary by Bet Type')
plt.xlabel('Bet Type')
plt.ylabel('Salary')
plt.xticks(rotation=45)
plt.show()

# Create a bar plot
sns.boxplot(x='Bet_Type_Preference', y='Salary', data=df, palette='viridis')
# Adding titles and labels
plt.title('Salary by Bet Type')
plt.xlabel('Bet Type')
plt.ylabel('Salary')
plt.xticks(rotation=45)
plt.show()


#Histogram
plt.figure(figsize=(10, 6))
sns.histplot(df['Total_Amount_Wagered'], bins=5, kde=True, color='blue')

#Adding titles and labels
plt.title('Total Amount Wagered')
plt.xlabel('Total Amount Wagered')
plt.ylabel('Amount Per bet')
plt.grid(True)#
plt.show()



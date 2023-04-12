# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 04:59:51 2023

@author: faisal
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("final.csv")
'''cleaning process starts from here'''
#print(df)
'''droping extra columns not with no name  '''
df.drop(columns=df.columns[0], axis=1, inplace=True)
#print(df)
'''droping extra columns not in use by using name  '''
df.drop(['Code', 'Cellular Subscription', 'No. of Internet Users', 'Broadband Subscription'], inplace=True, axis=1)
print(df)
df = df.dropna(how='all', axis=0)
print(df)
'''cleaning process ends here'''



'''
# Explore the statistical properties of the indicators using the describe method
print(df[['Country', 'Year', 'Internet Users(%)']].describe())

# Calculate the correlation matrix between the indicators
corr_matrix = df[['Country', 'Year', 'Internet Users(%)']].corr()
print(corr_matrix)

# Calculate the mean and standard deviation of each indicator for each region
region_means = df[['Country', 'Internet Users(%)']].groupby('Country').mean()
region_std = df[['Country', 'Internet Users(%)']].groupby('Country').std()

# Print the means and standard deviations
print(region_means)
print(region_std)
'''





# Filter the DataFrame to include only specific countries
countries = ['United States', 'China', 'India', 'Brazil']
df_filtered = df[df['Country'].isin(countries)]

# Create a bar graph of GDP for the selected countries
plt.bar(df_filtered['Country'], df_filtered['Internet Users(%)'])
plt.title('Internet Users(%) of selected countries')
plt.xlabel('Country')
plt.ylabel('Internet Users(%)')
plt.show()











# Read the CSV file into a Pandas DataFrame


# Filter the DataFrame to include only specific countries and years
countries = ['United States', 'China', 'India', 'Brazil']
years = [1990, 1999, 2010, 2015, 2020]
df_filtered = df[(df['Country'].isin(countries)) & (df['Year'].isin(years))]

# Create a bar graph of GDP for the selected countries and years
fig, ax = plt.subplots()
for i, year in enumerate(years):
    data = df_filtered[df_filtered['Year']==year]
    ax.bar(data['Country'], data['Internet Users(%)'], label=year)

ax.set_title('Internet Users(%) of selected countries by year')
ax.set_xlabel('Country')
ax.set_ylabel('Internet Users(%)')
ax.legend()
plt.show()



'''cleaning for mobile users'''

df = pd.read_csv("final.csv")
'''cleaning process starts from here'''
#print(df)
'''droping extra columns not with no name  '''
df.drop(columns=df.columns[0], axis=1, inplace=True)
#print(df)
'''droping extra columns not in use by using name  '''
df.drop(['Code', 'Internet Users(%)', 'No. of Internet Users', 'Broadband Subscription'], inplace=True, axis=1)
print(df)
df = df.dropna(how='all', axis=0)
print(df)
'''cleaning process ends here'''



# Filter the DataFrame to include only specific countries and years
countries = ['United States', 'China', 'India', 'Brazil']
years = [1990, 1999, 2010, 2015, 2020]
df_filtered = df[(df['Country'].isin(countries)) & (df['Year'].isin(years))]

# Create a bar graph of GDP for the selected countries and years
fig, ax = plt.subplots()
for i, year in enumerate(years):
    data = df_filtered[df_filtered['Year']==year]
    ax.bar(data['Country'], data['Cellular Subscription'], label=year)

ax.set_title('Cellular subscription of selected countries by year')
ax.set_xlabel('Country')
ax.set_ylabel('Cellular Subscription')
ax.legend()
plt.show()







# Filter the DataFrame to include only specific countries and years
countries = ['United States', 'China', 'India', 'Brazil']
years = [2010, 2015, 2020]
df_filtered = df[(df['Country'].isin(countries)) & (df['Year'].isin(years))]

# Create a bar graph of GDP for the selected countries and years
fig, ax = plt.subplots()
for country in countries:
    data = df_filtered[df_filtered['Country']==country]
    ax.bar(data['Cellular Subscription'], data['Country'], label=country)

ax.set_title('Cellular of selected countries by year')
ax.set_xlabel('Year')
ax.set_ylabel('Cellular Subscriber')
ax.legend()
plt.show()





# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('final.csv')

# Pivot the DataFrame to create a matrix of GDP values for each country and year
gdp_matrix = df.pivot(index='Country', columns='Year', values='Cellular Subscription')
us_row = gdp_matrix.loc['United States']
# Create a heat map using the Seaborn library
sns.heatmap(gdp_matrix, cmap='YlGnBu')

# Set the title and axis labels
plt.title('Mobile subscriptions by country and year')
plt.xlabel('Year')
plt.ylabel('Country')

# Show the plot
plt.show()

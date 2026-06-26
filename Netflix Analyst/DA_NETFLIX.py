import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('8. Netflix Dataset.csv')
print(data)

# Remove duplicate records
data[data.duplicated()]
data.drop_duplicates(inplace=True)
print(data[data.duplicated()])
print(data)

# Check for missing (null) values
print(data.isnull().sum())
data.fillna('Unknown', inplace=True)
print(data.isnull().sum())
print(data.isnull())

# Convert/standardize date format
data['Date_N'] = pd.to_datetime(data['Release_Date'], errors='coerce')
print(data.dtypes)
print(data)

# Count records by year with a filter for >= 2015
print(data['Date_N'].dt.year.value_counts())
data_filtered = data[data['Date_N'].dt.year >= 2015]
print(data_filtered)

# Analysis of the Number of Movies by Year
year_counts = data_filtered['Date_N'].dt.year.value_counts().sort_index()

plt.figure(figsize=(10,5))
plt.plot(year_counts.index, year_counts.values, marker='o', color='red')
plt.xlabel('Year')                    
plt.ylabel('Number of Movies/Shows')          
plt.title('Number of Netflix Movies/Shows per Year')
[plt.text(x, y, str(y), ha='center', va='bottom') 
 for x, y in zip(year_counts.index, year_counts.values)]
plt.show()

# Analysis of Movies/Shows by Category
print(data.head(2))
Cat = data.groupby('Category')['Category'].count()

plt.figure(figsize=(10,5))
bars = plt.bar(Cat.index, Cat.values, color='black')
plt.xlabel('Count')
plt.ylabel('Category')
plt.title('Number of Movies/Shows per Category')
plt.bar_label(bars) 
plt.show()

print(data.dtypes)

# Analyze content distribution by country (Top 10 countries)
data.groupby('Country')['Country'].count().sort_values(ascending=False)
top10 = data['Country'].value_counts().head(10)
print(top10)

plt.figure(figsize=(10,5))
bars = plt.barh(top10.index, top10.values, color='red')
plt.xlabel('Count')
plt.ylabel('Country')
plt.title('Top 10 Country for Movies/Show')
plt.bar_label(bars) 
plt.show()

# Analyze Show/Movie per Rating 
rating_counts = data['Rating'].value_counts()
Rat = data.groupby('Rating')['Rating'].count().sort_values(ascending=False)
print(Rat)
plt.figure(figsize=(14,5))
bars = plt.bar(Rat.index, Rat.values, color='red')
plt.xlabel('Count')
plt.ylabel('Rating')
plt.title('Number of Movies/Shows per Category')
plt.bar_label(bars) 
plt.show()

#Analyze Table for Category, Rating, and Count of Movies/Show
Table = data.groupby(['Rating', 'Category']).size().unstack(fill_value=0)
Table['Total'] = Table.sum(axis=1)
Table = Table.sort_values(by='Total', ascending=False)
Table_reset = Table.reset_index()
fig, ax = plt.subplots(figsize=(7,4))
ax.axis('off')
table = ax.table(
    cellText=Table_reset.values,
    colLabels=Table_reset.columns,
    rowLabels=Table_reset.index,
    loc='center')
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1, 1)
plt.title('Rating vs Category', fontsize=14)
plt.show()

#KPI
total_movies = data[data['Category'] == 'Movie'].shape[0]
total_tvshows = data[data['Category'] == 'TV Show'].shape[0]

movies = data[data['Category'] == 'Movie'].copy()
movies['Duration_Min'] = movies['Duration'].str.extract('(\d+)').astype(float)
avg_duration = movies['Duration_Min'].mean()


total_negara = data['Country'].nunique()

print("Netflix KPI")
print(f"Total Movies     : {total_movies}")
print(f"Total TV Shows   : {total_tvshows}")
print(f"Avg Duration     : {avg_duration:.2f} minutes")
print(f"Total Countries  : {total_negara}")




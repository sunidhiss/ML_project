import pandas as pd
# loading the dataset
df = pd.read_excel("ML_project/Final_data.xlsx")

print(df.info())

# cleaning the dataset
df = df.drop(columns=['Unnamed: 0'])

num_cols = ['Cases','Temp','Deaths','mon','Latitude','Longitude','preci','LAI']
for col in num_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

df = df.drop(columns=['Deaths'])

fill_cols = ['Cases','preci','Temp','LAI']
for col in fill_cols:
    df[col]=df[col].fillna(df[col].mean())

print(df.isnull().sum())
print(df.info())
print(df.head())

# analysis of the dataset

# 1.Monthly Analysis
mon_cases=df.groupby('mon')['Cases'].mean()
print(mon_cases)
mon_dis=df.groupby(['mon','Disease'])['Cases'].mean()
print(mon_dis)
mon_state=df.groupby(['mon','state_ut'])['Cases'].mean()
print(mon_state)

# 2.Disease Analysis
disease_cases = df.groupby('Disease')['Cases'].mean()
print(disease_cases)

import matplotlib.pyplot as plt

# month wise trend
monthly_cases = df.groupby('mon')['Cases'].mean()
monthly_cases.plot(kind='bar', figsize=(10,5))
plt.xlabel("Month")
plt.ylabel("Average Cases")
plt.title("Monthly Disease Trend")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("monthly_trend.png")
plt.show()

# disease wise trend
df['Disease'] = df['Disease'].str.lower()

df['Disease'] = df['Disease'].replace({
    'suspected dengue': 'dengue',
    'dengue and chikungunya': 'dengue',
    'dengue fever': 'dengue',
    'suspected chikungunya': 'chikungunya',
    'acute diarrhoeal disease': 'add',
    'diarrhea': 'add',
    'gastroenteritis': 'add'
})

disease_cases = df.groupby('Disease')['Cases'].mean()
disease_cases.plot(kind='bar', figsize=(12,6))
plt.title("Disease-wise Average Cases")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("disease_analysis.png")
plt.show()

# water vector analysis
def classify_disease(d):
    if 'dengue' in d or 'malaria' in d or 'chikungunya' in d:
        return 'Vector'
    else:
        return 'Water'

df['Type'] = df['Disease'].apply(classify_disease)
type_cases = df.groupby('Type')['Cases'].mean()
type_cases.plot(kind='bar', figsize=(6,4))
plt.title("Vector vs Water Borne Diseases")
plt.savefig("water_vector_analysis.png")
plt.show()

# correlation analysis
import seaborn as sns
corr = df[['Cases','Temp','preci','LAI']].corr()
sns.heatmap(corr, annot=True)
plt.title("Correlation Matrix")
plt.savefig("correlation_matrix.png")
plt.show()

# top 10 high risk districts
top_districts = df.groupby('district')['Cases'].mean().sort_values(ascending=False).head(10)
top_districts.plot(kind='bar', figsize=(10,5))
plt.title("Top 10 High Risk Districts")
plt.xticks(rotation=45)
plt.savefig("top_districts.png")
plt.show()


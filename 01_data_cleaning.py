# Sales Data Analysis
# Analyze a dataset containing sales information 
# Generate baisc insights such as total sales, top-selling and products and trends over time.
# Tools : Python(Pandas,Numpy,Matplotlib,Seaborn)or Excel.

# Import modules
import pandas as pd
import numpy as np 

# read File
df = pd.read_csv("01_sales_data.csv")
print(df.head())

# numerical data summary and information of null values

print(df.describe())
print(df.info())

# check null values 
print(df.isnull().sum()) # Every column handle 7 null values.

# Cleaning data Using fillna method and dropna method

df["Quantity"] = df["Quantity"].fillna(df["Quantity"].mean())
df["Quantity"] = df["Quantity"].astype(int)
print(df["Quantity"])

df['Unit_Price'] = df["Unit_Price"].fillna(df["Unit_Price"].mean())
df["Unit_Price"] = df["Unit_Price"].astype(int)
print(df['Unit_Price'])

df['Total_Sales'] = df["Total_Sales"].fillna(df["Total_Sales"].mean())
df["Total_Sales"] = df["Total_Sales"].astype(int)
print(df["Total_Sales"])

print(df.isnull().sum())

print(df)

# df.loc[(df['Product']=='T-Shirt')& (df['Category'].isna()),'Category'] = "Clothing"
# df.loc[(df['Product']=='Shoes')& (df['Category'].isna()),'Category'] = "Clothing"
# print(df)
# print(df.isnull().sum())


print(df.isnull().sum())

# Drop null values 
df= df.dropna().reset_index(drop=True)
print(df)

# Change the file name add new clean file

df.to_csv("Clean_sales_data.csv",index=False)

print(df.isnull().sum())
# Import Modules For Visualization 
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("02_Clean_sales_data.csv",parse_dates=['Date'])
print(df.isnull().sum())


# Total Sales : By Region and Category
# Aggregate data
sales_by_region = df.groupby('Region')['Total_Sales'].sum().reset_index()
sales_by_category = df.groupby('Category')['Total_Sales'].sum().reset_index()

# Plotting two subplots side by side
sns.set_style("whitegrid")
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 7))

# Subplot 1: By Region 
sns.barplot(data=sales_by_region, x='Region', y='Total_Sales', ax=ax1, palette='Blues_d')
ax1.set_title('Total Sales by Region')
ax1.set_xlabel('Region')
ax1.set_ylabel('Total Sales')
ax1.tick_params(axis='x', rotation=45)

# Subplot 2: By Category
sns.barplot(data=sales_by_category, x='Category', y='Total_Sales', ax=ax2, palette='Greens_d')
ax2.set_title('Total Sales by Category')
ax2.set_xlabel('Category')
ax2.set_ylabel('Total Sales')
ax2.tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()

# Top 5 Product Sales
top_products = df.groupby('Product')['Total_Sales'].sum().reset_index().sort_values(by='Total_Sales', ascending=False)
top_n = 5
top_products = top_products.head(top_n)

plt.figure(figsize=(8,6))
sns.barplot(data=top_products, x='Product', y='Total_Sales', palette='coolwarm')
plt.title(f'Top {top_n} Products by Total Sales')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Trend Over Time
df_sorted = df.sort_values('Date')

plt.figure(figsize=(8,6))
sns.lineplot(data=df_sorted, x='Date', y='Total_Sales', marker='o')
plt.title('Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

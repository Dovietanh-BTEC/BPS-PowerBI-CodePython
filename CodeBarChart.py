import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV files
country_df = pd.read_csv('Country_table.txt')
customer_df = pd.read_csv('Customer_table.txt')
category_df = pd.read_csv('ProductCategory_table.txt')
product_df = pd.read_csv('Product_table.txt')
sale_df = pd.read_csv('Sale_table.txt')
trend_df = pd.read_csv('MarketTrend_table.txt')
access_df = pd.read_csv('WebsiteAccess_table.txt')

# Group the sales data by product category and calculate the total sales
sales_by_category = sale_df.merge(product_df[['Product ID', 'Category ID']], on='Product ID')
sales_by_category = sales_by_category.merge(category_df[['Category ID', 'Category Name']], on='Category ID')
sales_by_category = sales_by_category.groupby('Category Name')['Total Price'].sum().reset_index()

# Create a bar chart
plt.figure(figsize=(10, 6))
sales_by_category.plot(kind='bar', x='Category Name', y='Total Price')
plt.title('Total Sales by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.show()


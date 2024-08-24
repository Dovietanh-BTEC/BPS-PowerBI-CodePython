import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV files
country_df = pd.read_csv('Country_table.txt')
customer_df = pd.read_csv('Customer_table.txt')
category_df = pd.read_csv('ProductCategory_table.txt')
product_df = pd.read_csv('Product_table.txt')
sales_df = pd.read_csv('Sale_table.txt')
trend_df = pd.read_csv('MarketTrend_table.txt')
access_df = pd.read_csv('WebsiteAccess_table.txt')

# Create a pie chart
plt.figure(figsize=(10, 6))
category_df['Category Name'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Distribution of Product Categories')
plt.axis('equal')
plt.show()

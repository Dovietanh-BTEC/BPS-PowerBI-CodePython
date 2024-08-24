import pandas as pd

# Load the CSV files
country_df = pd.read_csv('Country_table.txt')
customer_df = pd.read_csv('Customer_table.txt')
category_df = pd.read_csv('ProductCategory_table.txt')
product_df = pd.read_csv('Product_table.txt')
sale_df = pd.read_csv('Sale_table.txt')
trend_df = pd.read_csv('MarketTrend_table.txt')
access_df = pd.read_csv('WebsiteAccess_table.txt')

# Print the first few rows of each dataframe
print("Country DataFrame:")
print(country_df.head())
print("\nCustomer DataFrame:")
print(customer_df.head())
print("\nProduct Category DataFrame:")
print(category_df.head())
print("\nProduct DataFrame:")
print(product_df.head())
print("\nSale DataFrame:")
print(sale_df.head())
print("\nMarket Trend DataFrame:")
print(trend_df.head())
print("\nWebsite Access DataFrame:")
print(access_df.head())

# Check for missing values
print("Missing values in each dataframe:")
print("Country DataFrame:", country_df.isnull().sum())
print("Customer DataFrame:", customer_df.isnull().sum())
print("Product Category DataFrame:", category_df.isnull().sum())
print("Product DataFrame:", product_df.isnull().sum())
print("Sale DataFrame:", sale_df.isnull().sum())
print("Market Trend DataFrame:", trend_df.isnull().sum())
print("Website Access DataFrame:", access_df.isnull().sum())

sale_df['Sale Date'] = pd.to_datetime(sale_df['Sale Date'])


# Calculate the IQR
q1 = product_df['Price'].quantile(0.25)
q3 = product_df['Price'].quantile(0.75)
iqr = q3 - q1

# Identify outliers
outliers = product_df[(product_df['Price'] < q1 - 1.5 * iqr) | (product_df['Price'] > q3 + 1.5 * iqr)]
print("Outliers in Price column:", outliers)

# Remove outliers
product_df = product_df[~((product_df['Price'] < q1 - 1.5 * iqr) | (product_df['Price'] > q3 + 1.5 * iqr))]
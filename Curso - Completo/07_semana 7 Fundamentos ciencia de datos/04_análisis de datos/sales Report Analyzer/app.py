import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        print("Data loaded successfully!")
        return data
    except Exception as e:
        print("Error loading data:",e)
        return None
    
def clean_data(data):
    print("\nCleaning Data...")

    # Fill Missing Values
    data['Product_Category'] = data['Product_Category'].fillna("Unknown")
    data = data.dropna()

    # Convert Columns
    data['Date'] = pd.to_datetime(data['Date'])
    data['Sales_Amount'] = pd.to_numeric(data['Sales_Amount'], errors='coerce')

    # Add New Columns
    data['Year_Month'] = data['Date'].dt.to_period('M')
    if 'Quantity' in data.columns and 'Price' in data.columns:
        data['Revenue'] = data['Quantity'] * data['Price']

    print("Data cleaned successfully")
    return data

def analyze_data(data):
    print("\n--- Sales Insights ---")

    # Total sales by Month
    monthly_sales = data.groupby('Year_Month')['Sales_Amount'].sum()
    print("\nMonthly Sales:")
    print(monthly_sales)

    # Top 5 Products by Revenue
    if 'Revenue' in data.columns:
        top_products = data.groupby("Product_Name")["Revenue"].sum().sort_values(ascending=False).head(5)
        print("\nTop 5 Products by Revenue:")
        print(top_products)

    # Visualize Montly Sales
    monthly_sales.plot(kind="bar", figsize=(10, 6), color="skyblue")
    plt.title("Montly Sales")
    plt.xlabel("Month")
    plt.ylabel("Total Sales")
    plt.xticks(rotation=45)
    plt.show()

def main():
    print("Welcome to the Sales Report Analyzer!")

    # Load Data
    file_path = input("Enter the path to your sales CSV file: ")
    data = load_data(file_path)
    if data is None:
        return
    
    # Clean Data
    data = clean_data(data)

    # Analize Data
    analyze_data(data)

if __name__ == "__main__":
    main()
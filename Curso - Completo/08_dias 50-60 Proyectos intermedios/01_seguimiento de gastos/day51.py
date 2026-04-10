import os
import csv
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, 'expenses.csv')

def log_expense(category, amount, description):
    with open(FILE_PATH, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().strftime("%Y-%m-%d"), category, amount, description])

def load_expense():
    return pd.read_csv(FILE_PATH, names=['Date','Category','Amount','Description'])

def summarize_expenses(df):
    summary = df.groupby('Category')['Amount'].sum()
    print('\nExpense Summary:')
    print(summary)

def plot_expenses_by_category(df):
    summary = df.groupby('Category')['Amount'].sum()
    summary.plot(kind='pie', autopct='%1.1f%%', figsize=(8,8), title='Expenses by Category')
    plt.ylabel('')
    plt.show()

def plot_montly_trends(df):
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.to_period('M')
    monthly_summary = df.groupby('Month')['Amount'].sum()
    monthly_summary.plot(kind='bar', figsize=(10,6), title='Monthly Expense Trends')
    plt.xlabel('Month')
    plt.ylabel('Total Expenses')
    plt.xticks(rotation=45)
    plt.show()

def main():
    print('Welcome to the Expense Tracker')
    while True:
        print('\nOptions:')
        print('1. Log an Expense')
        print('2. View Expense Summary')
        print('3. Plot Expense by Category')
        print('4. Plot Monthly Trends')
        print('5. Exit')

        choice = input('Enter your choice (1-5):')
        if choice == '1':
            category = input('Enter category:')
            amount = float(input('Enter amount:'))
            description = input('Enter description:')
            log_expense(category,amount,description)
            print('Expense logged successfully!')
        elif choice == '2':
            df = load_expense()
            summarize_expenses(df)
        elif choice == '3':
            df = load_expense()
            plot_expenses_by_category(df)
        elif choice == '4':
            df = load_expense()
            plot_montly_trends(df)
        elif choice == '5':
            print('Goodbye')
            break
        else: 
            print('Invalid choice. Please try again (1-5).')

if __name__ == "__main__":
    main()
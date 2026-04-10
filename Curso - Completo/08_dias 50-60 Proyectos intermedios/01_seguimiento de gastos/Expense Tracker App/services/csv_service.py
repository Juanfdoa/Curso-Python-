import os
import io
import csv
import uuid
from datetime import datetime
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, 'expenses.csv')

def log_expense(category, amount, description):
    with open(FILE_PATH, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(
            [
                str(uuid.uuid4()),
                datetime.now().strftime("%Y-%m-%d"), 
                category, 
                amount, 
                description
            ]
        )

def load_expenses():
    if not os.path.exists(FILE_PATH):
        return pd.DataFrame(columns=['Id','Date','Category','Amount','Description'])

    df = pd.read_csv(FILE_PATH)
    df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce').fillna(0).astype(int)
    
    return df

def delete_expense(expense_id):
    df = load_expenses()
    df = df[df['Id'] != expense_id]
    df.to_csv(FILE_PATH, index=False)

def export_to_excel(df):
    output = io.BytesIO()
    df.to_excel(output, index=False, sheet_name='Expenses')
    output.seek(0)
    return output
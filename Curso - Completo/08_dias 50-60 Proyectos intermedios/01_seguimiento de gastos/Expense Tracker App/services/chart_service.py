import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import plotly.io as pio

def plot_expenses_by_category(df):
    df = df.copy()
    df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')
    summary = df.groupby('Category')['Amount'].sum().reset_index()
    fig = px.pie(
        summary,
        values='Amount',
        names='Category',
        title='Expenses by Category'
    )
    fig.update_layout(height=350)
    return pio.to_json(fig)

def plot_monthly_trends(df):
    df = df.copy()
    df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.strftime('%Y-%m')
    monthly = df.groupby('Month')['Amount'].sum().reset_index()

    fig = px.bar(monthly, x='Month', y='Amount', title='Monthly Expense Trends')
    fig.update_layout(
        height=350,
        bargap=0.6,
        xaxis_title='Month',
        yaxis_title='Amount',
        xaxis=dict(type='category')
    )
    return pio.to_json(fig)
from flask import Blueprint, render_template, request, redirect, url_for, send_file
from services.csv_service import log_expense, load_expenses, delete_expense, export_to_excel
from services.chart_service import plot_expenses_by_category, plot_monthly_trends

expenses_bp = Blueprint('expenses', __name__)

@expenses_bp.route('/', methods=['GET', 'POST'])
def home():
    categories = ["Food", "Transport", "Housing", "Utilities", "Education", "Health", "Entertainment", "Other"]

    if request.method == 'POST':
        category = request.form.get('category')
        amount = request.form.get('amount')
        description = request.form.get('description')

        if category and amount:
            try:
                amount = float(amount)
                log_expense(category, amount, description)
                return redirect(url_for('expenses.home'))
            except ValueError:
                pass

    df = load_expenses()
    return render_template(
        'index.html', 
        categories=categories, 
        df=df,
        pie=plot_expenses_by_category(df.copy()),
        bar=plot_monthly_trends(df.copy()))

@expenses_bp.route('/delete/<id>', methods=['POST'])
def delete(id):
    delete_expense(id)
    return redirect(url_for('expenses.home'))

@expenses_bp.route('/export')
def export():
    df = load_expenses()
    path = export_to_excel(df)
    return send_file(path, as_attachment=True, download_name='expenses.xlsx')
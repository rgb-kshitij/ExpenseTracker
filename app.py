from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database setup
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
db = SQLAlchemy(app)

# Expense Model
class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.String(20), nullable=False)

# Create database tables
with app.app_context():
    db.create_all()

@app.route('/', methods=['GET'])
def home():
    expenses = Expense.query.all()
    return render_template("index.html", expenses=expenses)

@app.route('/add', methods=['POST'])
def add():
    category = request.form['category']
    amount = request.form['amount']
    date = request.form['date']

    new_expense = Expense(category=category, amount=float(amount), date=date)
    db.session.add(new_expense)
    db.session.commit()

    return redirect('/')


@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    expense = Expense.query.get_or_404(id)
    db.session.delete(expense)
    db.session.commit()
    return redirect('/')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    expense = Expense.query.get_or_404(id)

    if request.method == 'POST':
        expense.category = request.form['category']
        expense.amount = float(request.form['amount'])
        expense.date = request.form['date']

        db.session.commit()
        return redirect('/')

    return render_template("edit.html", expense=expense)


import pandas as pd
import plotly.express as px

@app.route('/dashboard')
def dashboard():
    expenses = Expense.query.all()

    # Convert DB entries to pandas dataframe
    data = [{"category": e.category, "amount": e.amount, "date": e.date} for e in expenses]
    df = pd.DataFrame(data)

    if df.empty:
        return render_template("dashboard.html", message="No data to show yet 👀")

    # Pie chart (Spending by Category)
    fig1 = px.pie(df, names='category', values='amount', title='Spending by Category')
    pie_chart = fig1.to_html(full_html=False)

    # Bar chart (Amounts)
    fig2 = px.bar(df, x='date', y='amount', title='Expense Timeline')
    bar_chart = fig2.to_html(full_html=False)

    return render_template("dashboard.html", pie_chart=pie_chart, bar_chart=bar_chart)


if __name__ == "__main__":
    app.run(debug=True)

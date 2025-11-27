from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, request, redirect, flash


app = Flask(__name__)

app.secret_key = "super_secret_123"


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


# Database setup
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
db = SQLAlchemy(app)

#  user + expense models
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)


class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.String(20), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


#  Flask Login loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Create database tables
with app.app_context():
    db.create_all()

@app.route('/')
@login_required
def home():
    expenses = Expense.query.filter_by(user_id=current_user.id).all()
    return render_template("index.html", expenses=expenses)


@app.route('/add', methods=['POST'])
@login_required
def add():
     new_expense = Expense(
        category=request.form['category'],
        amount=float(request.form['amount']),
        date=request.form['date'],
        user_id=current_user.id
    )
     db.session.add(new_expense)
     db.session.commit()
     flash("Expense added successfully! 💰", "success")
     return redirect('/')



@app.route('/delete/<int:id>', methods=['POST'])
@login_required
def delete(id):
    expense = Expense.query.get_or_404(id)
    db.session.delete(expense)
    db.session.commit()
    flash("Expense deleted 🗑️", "warning")
    return redirect('/')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    expense = Expense.query.get_or_404(id)

    if request.method == 'POST':
        expense.category = request.form['category']
        expense.amount = float(request.form['amount'])
        expense.date = request.form['date']

        db.session.commit()
        flash("Expense updated ✏️", "info")
        return redirect('/')

    return render_template("edit.html", expense=expense)


import pandas as pd
import plotly.express as px

@app.route('/dashboard')
@login_required
def dashboard():
    expenses = Expense.query.filter_by(user_id=current_user.id).all()

    if not expenses:
        return render_template("dashboard.html", message="No data yet 👀")

    # Convert DB to DataFrame
    data = [{"category": e.category, "amount": e.amount, "date": e.date} for e in expenses]
    df = pd.DataFrame(data)

    # Ensure proper date format
    df['date'] = pd.to_datetime(df['date'])

    # Pie Chart: Category Distribution
    fig1 = px.pie(df, names='category', values='amount', title='Spending by Category')
    pie_chart = fig1.to_html(full_html=False)

    # Bar Chart: Spending History
    fig2 = px.bar(df, x='date', y='amount', title='Expense Timeline')
    bar_chart = fig2.to_html(full_html=False)

    return render_template("dashboard.html", pie_chart=pie_chart, bar_chart=bar_chart)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'], method="pbkdf2:sha256")

        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()

        flash("Account created successfully! Please log in 👌", "success")
        return redirect('/login')

    return render_template("signup.html")



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            flash("Welcome back! 👋", "success")
            return redirect('/')
        
        flash("❌ Wrong username or password!", "danger")
        return redirect('/login')

    
    return render_template("login.html")



@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logged out successfully 👋", "info")
    return redirect('/login')

from flask import Response
import csv
from datetime import datetime
import io

@app.route('/export')
@login_required
def export():
    expenses = Expense.query.filter_by(user_id=current_user.id).all()

    if not expenses:
        flash("⚠ No data to export!", "warning")
        return redirect('/')

    # Create an in-memory file
    output = io.StringIO()
    writer = csv.writer(output)

    # Header row
    writer.writerow(["Category", "Amount (₹)", "Date"])

    # Write database values
    for e in expenses:
        writer.writerow([e.category, e.amount, e.date])

    # Move cursor to start
    output.seek(0)

    # Send as downloadable file
    return Response(
        output.getvalue(),
        mimetype="text/csv",
        headers={
            "Content-Disposition": f"attachment; filename={current_user.username}_expenses_{datetime.now().strftime('%Y-%m-%d')}.csv"
        }
    )




if __name__ == "__main__":
    app.run(debug=True)


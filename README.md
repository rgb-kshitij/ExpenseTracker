# 💰 Expense Tracker

A full-stack web application to record, manage, and analyze expenses with authentication, dashboard analytics, CSV export, and Light/Dark mode.

---

## 📌 Table of Contents
- [Live Demo](#live-demo)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Folder Structure](#folder-structure)
- [Why I Built This](#why-i-built-this)
- [Future Improvements](#future-improvements)
- [License](#license)

---

## Live Demo

🔗 https://expensetracker-6h90.onrender.com  
(Sign up to use.)

---

## Features

- User authentication (Signup/Login/Logout)
- Add, edit, and delete expenses
- CSV export support
- Dashboard with visual analytics (Plotly)
- Dark/Light mode (saved in browser)
- Flash notifications
- Responsive UI with Bootstrap

---

## Tech Stack

| Category | Tools |
|----------|-------|
| Backend | Flask (Python) |
| Database | SQLite |
| Frontend | HTML, CSS, Bootstrap |
| Authentication | Flask-Login |
| Charts | Plotly Express |
| Deployment | Render |
| Version Control | Git & GitHub |

---

## Installation

```sh
git clone https://github.com/rgb-kshitij/ExpenseTracker.git
cd ExpenseTracker
pip install -r requirements.txt
python app.py
```

## Folder Structure

ExpenseTracker/
│── static/
│   └── theme.css
│── templates/
│   ├── index.html
│   ├── login.html
│   ├── signup.html
│   ├── edit.html
│   └── dashboard.html
│── instance/
│   └── expenses.db (auto-created)
│── app.py
│── requirements.txt
│── Procfile
│── README.md

---

## Why I Built This

I built this project to understand real-world development concepts including:
  -User authentication
  -Protected routes
  -Database handling
  -Charts and visual insights
  -Deployment workflow
 Instead of a simple CRUD project, I wanted a polished, useful application that feels like a      real product.

---

 ## Future Improvements

  -Monthly expense summary
  -Budget alerts
  -PDF export support
  -Custom categories with icons
  -PostgreSQL deployment version
  -Mobile app version (Flutter/React Native)

  ---

 ## License

  MIT License — free to use, modify, and distribute.


⭐ If you like this project, consider giving it a star!


Built by Kshitij Raj

# 💰 Expense Tracker Web App

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Flask](https://img.shields.io/badge/Framework-Flask-lightgrey)
![SQLite](https://img.shields.io/badge/Database-SQLite-green)
![Status](https://img.shields.io/badge/Status-Deployed-brightgreen)
![License](https://img.shields.io/badge/License-MIT-blue)

A full-stack expense tracking application where users can securely log in, add expenses, edit/delete records, download data as CSV, and visualize spending patterns through charts — all with a clean light/dark mode UI.

# 📑 Table of Contents

- [✨ Features](#-features)  
- [🧠 Tech Stack](#-tech-stack)  
- [🚀 Live Demo](#-live-demo)  
- [📦 Installation](#-installation)  
- [🧾 Usage](#-usage)  
- [📊 Dashboard Preview](#-dashboard-preview)  
- [📂 Folder Structure](#-Folder-Structure)
- [📌 Why I Built This](#-why-i-built-this)
- ## 📌 Why I Built This

I wanted to learn how real web applications handle:

- Authentication  
- Databases  
- State management  
- UI/UX  
- Deployment  

Instead of a basic CRUD project, I built a fully functional expense manager with analytics, CSV export, and dark mode — something useful and production-ready.

- [🚧 Future Improvements](#-future-improvements)
- ## 🚧 Future Improvements

- [ ] Budget alerts  
- [ ] Category icons  
- [ ] Monthly summary report (PDF)  
- [ ] AI insights for spending habits  
- [ ] PostgreSQL version (for cloud persistence)

- [🤝 Contributing](#-contributing)  
- [📄 License](#-license)



# Features

✔ User authentication (Signup/Login/Logout)  
✔ Flash messages with animated toast notifications  
✔ Light/Dark mode toggle (saved in local storage)  
✔ Add, edit, and delete expenses  
✔ Download all expenses as CSV  
✔ Data stored per-user (no shared data)  
✔ Analytics dashboard with Plotly charts  
✔ Fully responsive Bootstrap UI  
✔ Hosted online using Render  



# Tech Stack

| Component | Technology |
|----------|------------|
| Backend | Flask (Python) |
| Frontend | HTML, Bootstrap, Jinja2 |
| Database | SQLite |
| Authentication | Flask-Login |
| Charts | Plotly Express |
| Deployment | Render |
| Version Control | Git & GitHub |

---

# 🚀 Live Demo

🔗 **https://expensetracker-6h90.onrender.com**

(Login required — you can create your own account.)

---

# 📦 Installation

git clone https://github.com/rgb-kshitij/ExpenseTracker.git
cd ExpenseTracker
pip install -r requirements.txt
python app.py

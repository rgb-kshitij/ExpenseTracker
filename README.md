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
- [📂 Folder Structure](#-folder-structure)  
- [📌 Why I Built This](#-why-i-built-this)  
- [🚧 Future Improvements](#-future-improvements)  
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

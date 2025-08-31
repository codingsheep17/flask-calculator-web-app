# 🧮 Flask Calculator Web App  

A **Flask-based calculator web application** that allows users to perform basic calculations, securely log in, and view their calculation history. Each user's history is stored in a **MySQL database** and displayed on their dashboard.  

---

## 🚀 Features  
- 🔑 User Authentication (Signup, Login, Logout)  
- 📝 Calculation history saved per user  
- 📊 History displayed with date & time (ordered by latest)  
- 🎨 Clean responsive UI with Bootstrap  
- 🔒 Secure credential management using `.env`  

---

## 🛠️ Tech Stack  
- **Backend:** Flask (Python)  
- **Database:** MySQL  
- **Frontend:** Jinja2 + Bootstrap  
- **Environment Management:** python-dotenv  

---

## 📂 Project Structure  
flask-calculator-web-app/
│── app.py # Main Flask app
│── db.py # Database connection helper
│── templates/ # HTML (Jinja2) templates
│ ├── index.html
│ ├── login.html
│ ├── signup.html
│ └── history.html
│── static/ # CSS, JS, Images
│── schema.sql # Database schema (tables for users + history)
│── requirements.txt # Project dependencies
│── .gitignore # Ignored files (.env, venv, pycache)

## ⚙️ Setup Instructions  

1. **Clone the repository**  
   ```bash
   git clone https://github.com/yourusername/flask-calculator-web-app.git
   cd flask-calculator-web-app
Create virtual environment & install dependencies

python -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)
pip install -r requirements.txt
Setup MySQL Database

Create a database in MySQL:

CREATE DATABASE calculator_web_db;
USE calculator_web_db;
Run the schema script:

source schema.sql;
Configure environment variables

Create a .env file in the root directory:

env
Copy code
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=yourpassword
DB_NAME=calculator_web_db
SECRET_KEY=your_secret_key
Run the app

🤝 Contributing

Pull requests are welcome! If you’d like to improve the app, feel free to fork the repo and submit a PR.

📜 License

This project is licensed under the MIT License.

👤 Author
Syed Hasseeb Shah (CodingSheep17)
📧 codingsheep17@gmail.com
Copy code
flask run
Open in your browser: http://localhost:5000

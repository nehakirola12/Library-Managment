# 📚 Library Management System (Python Project)

## 📌 Overview

This project is a simple **Library Management System** built using Python. It allows users to manage book records, issue and return books, and calculate fines for late returns. The system uses a **dictionary-based structure** for storing book data and provides a user-friendly menu interface.

---

## 🚀 Features

* 📖 View available and issued books
* 👨‍🎓 Issue books with:

  * Student name
  * Issue date
  * Duration (in days)
* 📅 Automatic due date calculation
* 🔁 Return books with fine calculation
* ⚠️ Progressive fine system (₹10 per week for late returns)
* 📄 View all issued book records
* 🎯 Simple and interactive menu system

---

## 🛠️ Technologies Used

* Python (Core concepts)

  * Classes & Objects
  * Dictionaries
  * Functions
  * Loops & Conditionals
  * `datetime` module

---

## 📂 Project Structure

```id="libread1"
Library-Management-System/
│
├── library.py     # Main Python program
└── README.md      # Project documentation
```

---

## ▶️ How to Run

1. Make sure Python is installed on your system.
2. Download or clone this project.
3. Open a terminal or command prompt.
4. Navigate to the project folder.
5. Run the program:

```id="libread2"
python library.py
```

---

## 🧠 How It Works

* Books are stored in a **dictionary** with IDs and availability status.
* When a book is issued:

  * The user enters student name and duration.
  * The system records the issue date and calculates the due date.
* When returning a book:

  * The system checks if it is late.
  * A fine is applied based on delay (₹10 per week).
* Issued books are tracked separately for easy management.

---

## 📌 Example Menu

```id="libread3"
====== 📚 LIBRARY MENU ======
1. View Books
2. Issue Book
3. Return Book
4. View Issued Books
5. Exit
```

---

## ⚠️ Limitations

* No database or file storage (data resets after exit)
* No authentication system (admin/user login)
* Limited book records (hardcoded data)

---

## 🌟 Future Improvements

* Add file/database storage for persistent data
* Implement user login system
* Add search and filter options
* Support multiple copies of books
* Build a graphical user interface (GUI)

---

## 👨‍💻 Author

Your Name

---

## 📜 License

This project is open-source and free to use for educational purposes.

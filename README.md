# 💰 Personal Expense Tracker

A simple **command-line based Personal Expense Tracker** built with Python. It allows users to record, view, search, delete, and analyze their expenses. Expense data is stored locally in a CSV file.

## 📌 Features

* ➕ Add a new expense
* 👀 View all recorded expenses
* 🗑️ Delete an expense
* 🔍 Search an expense using its ID
* 📅 Generate a monthly expense summary
* 📊 View category-wise spending
* 💾 Store expense data in a CSV file
* 🆔 Automatically generate expense IDs

## 🛠️ Technologies Used

* **Python**
* **CSV**
* **datetime**
* **OS**

## 📂 Project Structure

```text
Personal-Expense-Tracker/
│
├── main.py
├── expenses.csv
└── README.md
```

> `expenses.csv` is automatically created by the program if it does not already exist.

## ⚙️ How It Works

The application stores expense records in a CSV file with the following fields:

| Field       | Description                |
| ----------- | -------------------------- |
| ID          | Unique ID of the expense   |
| Amount      | Amount spent               |
| Category    | Expense category           |
| Description | Description of the expense |
| Date        | Date of the expense        |

The CSV file is initialized automatically with these columns when the application is started.

## 🚀 Installation

### 1. Clone the repository

```bash
git clone 
```

### 2. Open the project directory

```bash
cd Personal-Expense-Tracker
```

### 3. Run the application

```bash
python main.py
```

## 🖥️ Menu

When the program starts, it provides the following options:

```text
1. Add Expense
2. View Expenses
3. Delete Expense
4. Search Expenses
5. Monthly Summary
6. Category Wise Spending
7. Exit
```

These options correspond directly to the functions implemented in the program.

## ➕ Add Expense

Select option `1` to add a new expense.

You will be asked to enter:

```text
Enter Amount :-
Enter Category :-
Enter Description :-
Enter date :-
```

The expense is then stored in `expenses.csv` with a generated ID.

### Example

```text
Enter Amount :- 250
Enter Category :- Food
Enter Description :- Lunch
Enter date :- 03-10-2026

Expense Added Successfully !
```

## 👀 View Expenses

Select option `2` to display all recorded expenses.

The expenses are displayed in a formatted table containing:

* ID
* Amount
* Category
* Description
* Date

Example:

```text
======================================================================
                         EXPENSES
======================================================================
ID   AMOUNT      CATEGORY       DESCRIPTION              DATE
----------------------------------------------------------------------
1    ₹250.00     Food           Lunch                    03-10-2026
2    ₹100.00     Travel         Bus fare                 03-10-2026
======================================================================
```

## 🗑️ Delete Expense

Select option `3` to delete an expense using its ID.

After deletion, the program reassigns the IDs to maintain sequential numbering.

## 🔍 Search Expense

Select option `4` to search for an expense by its ID.

If the ID exists, the corresponding expense details are displayed. If it does not exist, the program displays:

```text
Id not Found !
```

## 📅 Monthly Summary

Select option `5` to generate a summary for a particular month and year.

The program calculates:

* Total expenses
* Number of expenses
* Average expense

The date is expected in the format:

```text
DD-MM-YYYY
```

### Example

```text
========================================
          MONTHLY SUMMARY
========================================
Month: 10/2026
Total Expenses  : ₹350.00
Number of Expenses : 2
Average Expense : ₹175.00
========================================
```

## 📊 Category-Wise Spending

Select option `6` to view the total amount spent in each category.

The program also displays the overall total spending.

### Example

```text
========================================
       CATEGORY-WISE SPENDING
========================================
Food                : ₹250.00
Travel              : ₹100.00
----------------------------------------
Total               : ₹350.00
========================================
```

## 💾 Data Storage

All expense records are stored locally in:

```text
expenses.csv
```

The program uses Python's built-in `csv` module to read and write expense data.

No external database is required.

## 📋 CSV Format

The stored data follows this structure:

```csv
Id,Amount,Category,Description,Date
1,250.0,Food,Lunch,03-10-2026
2,100.0,Travel,Bus fare,03-10-2026
```

## 🧠 Concepts Used

This project demonstrates several fundamental Python concepts:

* Functions
* Loops
* Conditional statements
* Lists
* Dictionaries
* File handling
* CSV file handling
* Exception-free input processing
* Date and time handling
* String formatting
* Basic data analysis

## 📦 Python Modules Used

### `os`

Used to check whether the CSV file exists before creating it.

### `csv`

Used to read and write expense records.

### `datetime`

Used to process expense dates and generate monthly summaries.

These modules are imported directly in the project.

## 🔮 Future Improvements

Possible improvements for future versions:

* Add input validation
* Add expense editing/updating
* Add budget management
* Add date-based expense searching
* Add graphical reports and charts
* Add sorting and filtering
* Add a GUI version
* Add database support such as SQLite
* Add data export options

## 🎯 Project Purpose

This project was created to practice Python programming concepts while building a practical command-line application for managing personal expenses.

## 👨‍💻 Author

**Yatharth Kaushik**

---

⭐ If you find this project useful, consider giving the repository a star!

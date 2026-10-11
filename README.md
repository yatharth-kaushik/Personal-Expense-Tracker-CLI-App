<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:11998e,100:38ef7d&height=220&section=header&text=Personal%20Expense%20Tracker&fontSize=48&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Track%20%E2%80%A2%20Analyze%20%E2%80%A2%20Save%20%E2%80%94%20right%20from%20your%20terminal&descAlignY=58&descSize=18" width="100%" />

<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&pause=1000&color=38EF7D&center=true&vCenter=true&width=650&lines=A+command-line+expense+manager+in+Python+%F0%9F%90%8D;Add%2C+search+and+delete+expenses+%F0%9F%92%B8;Monthly+summaries+%26+category+insights+%F0%9F%93%8A;Zero+dependencies.+Just+Python+%26+CSV+%E2%9C%A8" alt="Typing SVG" />
</a>

<br/>

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![CLI](https://img.shields.io/badge/Interface-CLI-black?style=for-the-badge&logo=gnubash&logoColor=white)
![Storage](https://img.shields.io/badge/Storage-CSV-217346?style=for-the-badge&logo=files&logoColor=white)
![Dependencies](https://img.shields.io/badge/Dependencies-None-brightgreen?style=for-the-badge)

<img src="https://img.shields.io/github/stars/yatharth-kaushik/Personal-Expense-Tracker?style=flat-square&logo=github&color=yellow" alt="stars" />
<img src="https://img.shields.io/github/forks/yatharth-kaushik/Personal-Expense-Tracker?style=flat-square&logo=github" alt="forks" />
<img src="https://img.shields.io/github/last-commit/yatharth-kaushik/Personal-Expense-Tracker?style=flat-square&color=blue" alt="last commit" />
<img src="https://img.shields.io/github/repo-size/yatharth-kaushik/Personal-Expense-Tracker?style=flat-square&color=orange" alt="repo size" />

</div>

---

## 📖 Overview

**Personal Expense Tracker** is a simple command-line application built with Python that helps you **record, view, search, delete, and analyze** your daily expenses. All data is stored locally in a CSV file, so there's no database to set up and nothing to install.

---

## ✨ Features

| | Feature | Description |
|---|---|---|
| ➕ | **Add Expense** | Record amount, category, description and date |
| 👀 | **View Expenses** | See everything in a neatly formatted table |
| 🗑️ | **Delete Expense** | Remove an entry; IDs are re-numbered automatically |
| 🔍 | **Search by ID** | Instantly look up a single expense |
| 📅 | **Monthly Summary** | Total, count and average for any month |
| 📊 | **Category Spending** | See how much you spend in each category |
| 💾 | **CSV Storage** | Data saved locally in `expenses.csv` |
| 🆔 | **Auto IDs** | Unique IDs generated for every expense |

---

## 🛠️ Built With

<div align="center">

<img src="https://skillicons.dev/icons?i=python,vscode,git,github&perline=4" alt="tech" />

</div>

`Python` • `csv` • `datetime` • `os`

---

## 🚀 Getting Started

**1️⃣ Clone the repository**

```bash
git clone https://github.com/yatharth-kaushik/Personal-Expense-Tracker.git
```

**2️⃣ Move into the project folder**

```bash
cd Personal-Expense-Tracker
```

**3️⃣ Run the app**

```bash
python main.py
```

> 💡 `expenses.csv` is created automatically the first time you run the program.

---

## 🖥️ Main Menu

```text
1. Add Expense
2. View Expenses
3. Delete Expense
4. Search Expenses
5. Monthly Summary
6. Category Wise Spending
7. Exit
```

---

## 📸 Demo

<details open>
<summary><b>➕ Add Expense</b></summary>

```text
Enter Amount :- 250
Enter Category :- Food
Enter Description :- Lunch
Enter date :- 03-10-2026

Expense Added Successfully !
```

</details>

<details>
<summary><b>👀 View Expenses</b></summary>

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

</details>

<details>
<summary><b>🔍 Search Expense</b></summary>

Enter an ID to see its details. If it doesn't exist, you'll see:

```text
Id not Found !
```

</details>

<details>
<summary><b>📅 Monthly Summary</b></summary>

Enter a date in `DD-MM-YYYY` format to get that month's report.

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

</details>

<details>
<summary><b>📊 Category-Wise Spending</b></summary>

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

</details>

---

## 📂 Project Structure

```text
Personal-Expense-Tracker/
│
├── main.py          # Application code
├── expenses.csv     # Auto-generated expense data
└── README.md        # Project documentation
```

---

## 💾 Data Format

Expenses are stored in `expenses.csv`:

| Field | Description |
|---|---|
| `Id` | Unique ID of the expense |
| `Amount` | Amount spent |
| `Category` | Expense category |
| `Description` | What the expense was for |
| `Date` | Date of the expense (`DD-MM-YYYY`) |

```csv
Id,Amount,Category,Description,Date
1,250.0,Food,Lunch,03-10-2026
2,100.0,Travel,Bus fare,03-10-2026
```

---

## 🧠 Concepts Practiced

![Functions](https://img.shields.io/badge/Functions-informational?style=flat-square)
![Loops](https://img.shields.io/badge/Loops-informational?style=flat-square)
![Conditionals](https://img.shields.io/badge/Conditionals-informational?style=flat-square)
![Lists](https://img.shields.io/badge/Lists-informational?style=flat-square)
![Dictionaries](https://img.shields.io/badge/Dictionaries-informational?style=flat-square)
![File Handling](https://img.shields.io/badge/File%20Handling-informational?style=flat-square)
![CSV](https://img.shields.io/badge/CSV-informational?style=flat-square)
![Date & Time](https://img.shields.io/badge/Date%20%26%20Time-informational?style=flat-square)
![String Formatting](https://img.shields.io/badge/String%20Formatting-informational?style=flat-square)
![Data Analysis](https://img.shields.io/badge/Basic%20Data%20Analysis-informational?style=flat-square)

---

## 🔮 Roadmap

- [ ] Input validation
- [ ] Edit / update expenses
- [ ] Budget management
- [ ] Search by date
- [ ] Graphical reports and charts
- [ ] Sorting and filtering
- [ ] GUI version
- [ ] SQLite database support
- [ ] Export data

---

## 🎯 Project Purpose

Created to practice Python programming concepts while building a practical command-line application for managing personal expenses.

---

## 👨‍💻 Author

<div align="center">

**Yatharth Kaushik**

<a href="https://github.com/yatharth-kaushik"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" /></a>
<a href="https://www.linkedin.com/in/yatharth-kaushik-92920a421/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" /></a>

<br/><br/>

⭐ **If you find this project useful, consider giving it a star!** ⭐

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:38ef7d,100:11998e&height=120&section=footer" width="100%" />

</div>

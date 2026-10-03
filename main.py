import os,csv
from datetime import datetime
print("Hello! Welcome to Personal Expense Tracker")
print("What you want to do ?")
expenses="expenses.csv"
def initialise():
    if not os.path.exists(expenses):
        with open(expenses,"w",newline="") as f:
            writer=csv.writer(f)
            writer.writerow(["Id","Amount","Category","Description","Date"])
def get_next_id():
    with open(expenses, "r", newline="") as f:
        reader = csv.DictReader(f)
        ids = [int(row["Id"]) for row in reader]

    if not ids:
        return 1

    return max(ids) + 1       
def addExpense():
    id = get_next_id()
    amount=float(input("Enter Amount :- "))
    category = input("Enter Category :- ")
    description = input("Enter Description :- ")
    date = input("Enter date :- ")
    with open(expenses,"a",newline="") as f:
        writer=csv.writer(f)
        writer.writerow([id,amount,category,description,date])
    print("Expense Added Successfully !")
def viewExpense():
    print("\n" + "=" * 70)
    print(" " * 25 + "EXPENSES")
    print("=" * 70)

    with open(expenses, "r", newline="") as f:
        reader = csv.DictReader(f)

        rows = list(reader)

        if not rows:
            print("No expenses found.")
            print("=" * 70)
            return

        print(f"{'ID':<5}{'AMOUNT':<12}{'CATEGORY':<15}{'DESCRIPTION':<25}{'DATE':<12}")
        print("-" * 70)

        for row in rows:
            print(
                f"{row['Id']:<5}"
                f"₹{float(row['Amount']):<11.2f}"
                f"{row['Category']:<15}"
                f"{row['Description']:<25}"
                f"{row['Date']:<12}"
            )

    print("=" * 70)
def deleteExpense():
    del_id = input("Enter Id of Expense you want to delete :- ")

    rows = []
    found = False

    with open(expenses, "r", newline="") as f:
        reader = csv.DictReader(f)

        for i in reader:
            if i["Id"] == del_id:
                found = True
            else:
                rows.append(i)

    if found:

        # Reassign IDs
        for index, row in enumerate(rows, start=1):
            row["Id"] = index

        with open(expenses, "w", newline="") as f:
            fieldnames = ["Id", "Amount", "Category", "Description", "Date"]

            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

        print("Expense Deleted Successfully !")

    else:
        print("Expense Id not Found !")
def searchExpense():
    search_id = input("Enter Id of Expense you want to search :- ")
    found = False
    with open(expenses,"r") as f:
        reader=csv.DictReader(f)
        for i in reader:
            if i["Id"] == search_id:
                found=True
                print("\n" + "=" * 70)
                print(" " * 25 + "EXPENSES")
                print("=" * 70)
                print(f"{'ID':<5}{'AMOUNT':<12}{'CATEGORY':<15}{'DESCRIPTION':<25}{'DATE':<12}")
                print("-" * 70) 
                print(
                        f"{i['Id']:<5}"
                        f"₹{float(i['Amount']):<11.2f}"
                        f"{i['Category']:<15}"
                        f"{i['Description']:<25}"
                        f"{i['Date']:<12}"
                    )
                print("=" * 70)
    if found==False:
        print("Id not Found !")
def monthlySummary():
    month = int(input("Enter Month (MM) :- "))
    year = int(input("Enter Year (YYYY) :- "))
    total=0
    count=0
    with open(expenses,"r") as f:
        reader=csv.DictReader(f)
        for i in reader:
            expense_date= datetime.strptime(i["Date"],"%d-%m-%Y")
            if expense_date.month == month and expense_date.year == year :
                total=total + float(i["Amount"])
                count+=1
    print("\n" + "=" * 40)
    print("          MONTHLY SUMMARY")
    print("=" * 40)

    if count == 0:
        print("No expenses found for this month.")
    else:
        average = total / count

        print(f"Month: {month}/{year}")
        print(f"Total Expenses  : ₹{total:.2f}")
        print(f"Number of Expenses : {count}")
        print(f"Average Expense : ₹{average:.2f}")

    print("=" * 40)
def CategoryWiseSpending():
    category_total={}
    total=0
    with open(expenses,"r") as f:
        reader=csv.DictReader(f)
        for i in reader:
            category = i["Category"]
            amount=float(i["Amount"])
            if category in category_total:
                category_total[category]+=amount
            else:
                category_total[category]=amount
            total=total+amount
    print("\n" + "=" * 40)
    print("       CATEGORY-WISE SPENDING")
    print("=" * 40)

    if not category_total:
        print("No expenses found.")
    else:
        for category, amount in category_total.items():
            print(f"{category:<20}: ₹{amount:.2f}")

        print("-" * 40)
        print(f"{'Total':<20}: ₹{total:.2f}")

    print("=" * 40)
initialise()
while True:
    ch=input("""
1. Add Expense
2. View Expenses
3. Delete Expense
4. Search Expenses
5. Monthly Summary
6. Category Wise Spending 
7. Exit :- """)
    
    if ch=="1":
        addExpense()
    elif ch=="2":
        viewExpense()
    elif ch=="3":
        deleteExpense()
    elif ch=="4":
        searchExpense()
    elif ch=="5":
        monthlySummary()
    elif ch=="6":
        CategoryWiseSpending()
    elif ch == "7":
        break
    else:
        print("Invalid Choice !")
# Expense_tracker_project

# Expense Tracker Python Project

This Python project is designed to help users track their expenses efficiently. It allows users to input expense details, categorize them, and save them to a CSV file. The project also provides a summary of expenses, showing how much has been spent in each category, and calculates the remaining budget and the daily budget for the rest of the month.

# Features:

1. **User Input:**
   - The user begins by entering the **expense name** and the **amount** spent.
   - Next, the user selects an **expense category** from the following options:
     1. Food
     2. Home
     3. Work
     4. Fun
     5. Miscellaneous

2. **Saving Expenses:**
   - After the user provides the necessary details, the expense is saved to a CSV file (`expenses.csv`).
   - If the file already exists, the new expense is appended to it.
   - If the file does not exist, a new CSV file is created with appropriate headers before saving the expense.
   
3. **Expense Summary:**.
   - After saving the expense, the program summarizes the user's spending:
     - **Total Spent by Category:** The program calculates and displays the total amount spent in each category.
     - **Remaining Budget:** The program subtracts the total spent from the budget and displays the remaining amount.
     - **Remaining Days in the Month:** The program calculates how many days are left in the current month.
     - **Daily Budget for Remaining Days:** The program calculates the budget per day for the remaining days of the month based on the remaining budget.
This project provides a simple yet effective way for users to monitor their spending, ensuring they stay within their budget throughout the month.

Requirements: Python 3.x

Contributing: Feel free to submit issues or fork the repository and submit pull requests if you'd like to contribute.

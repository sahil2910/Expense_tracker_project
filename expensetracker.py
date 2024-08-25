from expense import Expense  #with this expense we can use the Expense class from expense.py here
import calendar
import datetime


def main():
    print(f"Running expense tracker")
    expense_file_path = "expenses.csv" # declaring file path/name 
    budget = 20000


    # get user input for expense
    expense = get_user_expense()
    #print(expense) we dont need this because its gonna be printed out when i save expense to file 

    # write their expense to a file
    save_expense_to_file(expense, expense_file_path) # we want to use the name path as a constant or a argument here we pass it as a argument


    # read file and summarize  expense
    summarize_user_expense(expense_file_path, budget)

def get_user_expense():
    print(f"Getting user Expense")
    expense_name = input("Enter a expense name:")
    expense_amount = float(input("Enter the amount :"))

    expense_categories = [
        " Food",
        " Home",
        " Work",
        " Fun",
        " Miscellaneous", 
    ]

    while True:
        print("Select a Category :")
        for i,category_name in enumerate(expense_categories): # enumerate function in list we ge a 2 pull response which is the index of an item and value ofthe item
            print(f"    {i + 1}.  {category_name}")

        value_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input(f"Enter a category number {value_range}: ")) -1

        if selected_index in range(len(expense_categories)):
            #break     intead of breaking the loop  we can return the value from here which will break the loop
            selected_category = expense_categories[selected_index] # we have the list of category and index to actually get the category name we create this meanin we dont have category selected by the user 
            new_expense = Expense(name = expense_name , category= selected_category ,amount= expense_amount ) #we are gonna construct it with the values that we have taken from the user 
            return new_expense        
        else:
            print("Invalid category. Please try again")


def save_expense_to_file(expense : Expense, expense_file_path): #to save something to a file we need to open the file and to open the file we need to know the file name 
    print(f"Saving user Expense: {expense} to {expense_file_path} ")
    with open(expense_file_path, "a") as f:    #opening the file 1st arrgument file path 2nd argument mode here "a" meaninng append which will add and not overwrite and if file doesnt exist we will create it
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")


def summarize_user_expense(expense_file_path , budget):
    print(f"Summarizing user Expense")
    expenses:list[Expense] = []
    with open (expense_file_path, "r") as f:    #here r means read only mode we want to read each line
        lines = f.readlines()   # f.readlines will give us a list we could enumerate 
        for line in lines:
            #print(line)  # here we have additional line spaces because when we read these lines we also reading the new line character that we cant see in expenses.csv but its causing new line to occur and because print also add a new line 
            stripped_line = line.strip()  #strip is use to remove white spaces from trailing and preciding
            expense_name , expense_amount, expense_category = stripped_line.split(",")
            line_expense  = Expense(name = expense_name , category= expense_category ,amount=float(expense_amount))
            expenses.append(line_expense)
    
    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category :
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount

    #print(amount_by_category) to print it nicely we can loop through it
    print("Expenses By Category")
    for key, amount in amount_by_category.items():
        print(f"   {key}: Rs{amount}")

    total_spent = sum([x.amount for x in expenses])
    print(f"Total spent: Rs{total_spent} ")

    Remaining_budget = budget - total_spent
    print(f"Budget Remaining: Rs{Remaining_budget}")


    now = datetime.datetime.now() # get current date time
    days_in_month = calendar.monthrange(now.year, now.month)[1] #Get the number  of days in the current month
    Remaining_days = days_in_month- now.day   #Calculate the remaining days in the current month
    print("Remaining days in the current month:", Remaining_days)

    daily_budget = Remaining_budget/ Remaining_days
    print(f"Budget Per Day : Rs{daily_budget:.2f}")


if __name__ == "__main__": # to make sure that this runs only when we run this file and not when we run it as part of another file
    main()    

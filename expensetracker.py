total = 0

print("Expense Tracker")
print("Type 'quit' to stop and see total")

while True:
    user_input = input("Enter expense amount: ")
    
    if user_input == "quit":
        break
    
    try:
        expense = int(user_input)
        total = total + expense
        print("Added! Current total:", total)
    except ValueError:
        print("Invalid input. Please enter a number.")

print("Total Spent:", total)
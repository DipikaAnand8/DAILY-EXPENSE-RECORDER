expenses = []

while(True):
    print("***** EXPENSE TRACKER *****")
    print("1. ADD EXPENSE")
    print("2. VIEW EXPENSE")
    print("3. TOTAL EXPENSES")
    print("4. EXIT")

    choice=int(input("enter your choice: "))

    if choice == 1:
        name = input("enter expense name: ")
        amt = float(input("enter the amount: "))

        expenses.append([name , amt])
        print("expense added successfully")

    elif choice == 2:
        print("your expenses: ")
        for item in expenses:
            print(f"{item[0]} : Rs. {item[1]}")

    elif choice == 3:
        total = 0
        for item in expenses:
            total += item[1]
        print("total expenses : Rs ", total)

    elif choice == 4:
        print("thankyou!")        
        break

    else:
        print("invalid choice! please try again")



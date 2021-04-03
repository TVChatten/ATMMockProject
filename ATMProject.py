import datetime
currentDatetime = datetime.datetime.now()
name = input("What is your name? \n")
allowedUsers = ['Shay','Mike','Love']
allowedPassword = ['PasswordShay','PasswordMike','PasswordLove']

if name in allowedUsers:
    password = input("What is your password \n")
    userID = allowedUsers.index(name)
    
    while True:

        if (password == allowedPassword[userID]):

            print("Welcome %s" %name)
            print("The current date and time is: " + str(currentDatetime))
            print("These are the available options:")
            print("1: Withdrawal")
            print("2: Cash Deposit")
            print("3: Complaint")

        selectedOption = int(input("Please select an option:"))

        if (selectedOption == 1):
            cashWithdrawal = float(input("How much would you like to withdraw?"))
            print("Take your cash.")

        elif (selectedOption == 2):
            cashDeposit = float(input("How much would you like to deposit?"))
            print('Your current balance is: ' + (str(cashDeposit)))

        elif (selectedOption == 3):
            custComplaint = input('What issue will you like to report?')
            print('Thank you for contacting us.')

        else:
            print("Invalid option selected. Please try again.")

    else:
        
        print("Password Incorrect, please try again.")
else:
    print("Name not found, please try again.")
    
import datetime
import random

database = {} #dictionary 

currentDatetime = datetime.datetime.now()


def init():

    isValidOptionSelected = False
    print("WELCOME TO THE CLOVER ATM")

    while isValidOptionSelected == False:
        haveAccount = int(input("Do you have an account with us?: 1 (yes) 2 (no) \n"))

        if(haveAccount == 1):
                isValidOptionSelected = True #make this true so that the loop doesn't run.
                print(login())

        elif(haveAccount == 2):
                isValidOptionSelected = True
                print(register())
        else:
            print("You have selected an invalid option")

def register():
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    full_name = (first_name + ' ' + last_name)
    email = input("What is your email \n")
    password = input('Create yourself a password. \n')
    accountNumber = generationAccountNumber()


    database[accountNumber] = [full_name, email, password]

    print("Account Number:")
    print(accountNumber)

    login()

 
def login():
     print("****LOGIN****")
     
     userAccountNumber = int(input('What is your account number? \n'))
     password = input('What is your password? \n')
     
     for accountNumber, userDetails in database.items():
        if(accountNumber == userAccountNumber):
            if(userDetails[2] == password):
                print('User is established.')
                establishedAccounts()
            else:
                print('Invalid account or password.')

def bankGreeting():
    print("The current date and time is: " + str(currentDatetime))
    print("These are the available options:")
    print("1: Withdrawal")
    print("2: Cash Deposit")
    print("3: Complaint")
    print("4: Logout")


def establishedAccounts():
    print("Welcome to the Clover ATM")

    bankGreeting()
    
    selectedOption = int(input("Please select an option:"))
    
    def cashWithdrawal():
        float(input("How much would you like to withdraw?"))
        return cashWithdrawal

    def cashDeposit():
        userDeposit = float(input("How much would you like to deposit?"))
        return userDeposit

    def custComplaint():
        input('What issue will you like to report?')
        return custComplaint

    if (selectedOption == 1):
        cashWithdrawal()
        print("Take your cash.")
        establishedAccounts()

    elif (selectedOption == 2):
        cashDeposit()
        print('Your amount was deposited.')
        establishedAccounts()

    elif (selectedOption == 3):
        custComplaint()
        print('Thank you for contacting us.')
        establishedAccounts()
    
    elif (selectedOption == 4):
        exit()
        
    else:
        print("Invalid option selected. Please try again.")
        establishedAccounts()

        

def generationAccountNumber():

    return random.randrange(1111111111,9999999999)

init()

    
import datetime
import random
import validation
import database
from getpass import getpass


# database = {} #dictionary


currentDatetime = datetime.datetime.now()

def init():

    isValidOptionSelected = False

    print("WELCOME TO THE CLOVER ATM")

    while isValidOptionSelected == False:

        haveAccount = int(
            input("Do you have an account with us?: 1 (yes) 2 (no) \n"))

        if(haveAccount == 1):

                # make this true so that the loop doesn't run.
                isValidOptionSelected = True

                print(login())

        elif(haveAccount == 2):

                isValidOptionSelected = True

                print(register())

        else:

            print("You have selected an invalid option")

def login():

     print("****LOGIN****")

     userAccountNumber = input('What is your account number? \n')

     is_valid_account_number = validation.accountNumberValidation(
         userAccountNumber)

     if is_valid_account_number:

         password = getpass("What is your password? \n")

         user = database.authenticated_user(userAccountNumber,password)

         if user:

             establishedAccounts(user)

         print('Invalid account or password')

         login()
        
     else:
            
            print('Invalid account or password. Check account number to make sure it''s 10 digits.')
            init()


def register():

    first_name = input("What is your first name? \n")

    last_name = input("What is your last name? \n")

    full_name = (first_name + ' ' + last_name)

    email = input("What is your email \n")

    password = getpass("Create yourself a password \n")

    account_balance = float(input("How much would you like to place for your initial balance?"))

    accountNumber = generationAccountNumber()

    is_user_created = database.create(
        accountNumber, first_name, last_name, full_name, email, password, account_balance)

    if is_user_created:

    # database[accountNumber] = [full_name, email, password]

    # use database module to create new user record

        print("Account Number:")

        print(accountNumber)

        login()

    else:
        print("Something went wrong. Please try again")
        register()



def bankGreeting():

    print("The current date and time is: " + str(currentDatetime))

    print("These are the available options:")

    print("1: Withdrawal")

    print("2: Cash Deposit")

    print("3: Complaint")

    print("4: Logout")

    print("5: Exit")



def establishedAccounts(user):

    print("Welcome to the Clover ATM %s %s " % (user[0], user[1]))


    bankGreeting()
    

    selectedOption = int(input("Please select an option:"))
    

    def cashWithdrawal(user):
        currentBalance = user[5]
        userWithdrawal = (float(input("How much would you like to withdraw?")))
        view_account_balance_withdrawal = float(currentBalance) - float(userWithdrawal)
        user[5] = view_account_balance_withdrawal
        


        print("Your total account balance now is:" +str(view_account_balance_withdrawal))


    def cashDeposit(user):
        currentBalance = user[5]
        userDeposit = (float(input("How much would you like to deposit?")))
        view_account_balance_deposit = userDeposit + float(user[5])
        user[5] = view_account_balance_deposit


    def custComplaint():

        input('What issue will you like to report?')

        return custComplaint


    if (selectedOption == 1):

        cashWithdrawal(user)

        database.newBalance_Withdrawal(user)

        print("Take your cash.")

        establishedAccounts(user)


    elif (selectedOption == 2):

        cashDeposit(user)

        database.newBalance_Deposit(user)

        print('Your amount was deposited.')

        establishedAccounts(user)


    elif (selectedOption == 3):

        custComplaint()

        print('Thank you for contacting us.')

        establishedAccounts()
    

    elif (selectedOption == 4):

        database.remove_authentication_file()

        login()

    elif (selectedOption == 5):

        database.remove_authentication_file()

        exit()
        

    else:

        print("Invalid option selected. Please try again.")

        establishedAccounts()

        


def generationAccountNumber():


    return random.randrange(1111111111,9999999999)



def logout(userAccountNumber):
    login()

init()

    

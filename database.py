#create record
#update record
#read record
#delete record

#search for user (find user)

import os
import validation

user_db_path = 'data/user_record/'
auth_db_path = 'data/auth_session/'


def create(userAccountNumber, first_name, last_name, full_name, email, password, account_balance):

    #create a file
    # name of file = account_number.txt
    # add the user details to the file 
    #return true
    #if saving to file fails, then delete created file.

    user_data = first_name + "," + last_name + "," + full_name + "," + email + "," + password + "," + str(account_balance)

    if does_account_number_exist(userAccountNumber):
        return False

    if does_email_exist(email):
        print("User already exists.")
        return False

    completion_state = False

    try:
        f = open(user_db_path + str(userAccountNumber) + ".txt", "x")
        
    except FileExistsError:
        
       does_file_contain_data = read(user_db_path + str(userAccountNumber) + ".txt")
       if not does_file_contain_data:
           delete(userAccountNumber)
        #delete the already created file and print out error. Then return false.
        #check content of file before deleting

    else:

        f.write(str(user_data));

        completion_state = True

    finally:

        f.close();

        return completion_state


def read(userAccountNumber):
    #find user with account number
    #fetch number of the file
    is_valid_account_number = validation.accountNumberValidation(userAccountNumber)

    try:
        
        if is_valid_account_number:
            f = open(user_db_path + str(userAccountNumber) + ".txt", "r")
        else:
            f = open(user_db_path + userAccountNumber, "r")

    except FileNotFoundError:

        print("Invalid account number format - file not found")

    except FileExistsError:

        print("User doesn't exist.")

    except TypeError:

        print("Invalid account number format.")

    else:

        return f.readline()

    return False


def update(userAccountNumber):
    print("Update user record")
    #find user with account number
    #fetch the content of the file
    #update the content of the file
    #save the file
    #return true


def delete(userAccountNumber):
    #find user with account number
    #delete the user record (file)
    #return true
    
    is_delete_successful = False

    if os.path.exists(user_db_path + str(userAccountNumber) + ".txt"):
        try:
            os.remove(user_db_path + str(userAccountNumber) + ".txt")
            is_delete_successful = True
        except FileNotFoundError:
            print("User not found.")
        finally:
            return is_delete_successful


def does_email_exist(email):
    
    all_users = os.listdir(user_db_path)

    for user in all_users:
        
       user_list = str.split(read(user), ",")

       if email in user_list:

            return True

    return False


def does_account_number_exist(accountNumber):
    
    all_users = os.listdir(user_db_path)

    for user in all_users:

        if user == str(accountNumber) + ".txt":

            return True

    return False



def authenticated_user(accountNumber, password):

    if does_account_number_exist(accountNumber):

        user = str.split(read(accountNumber), ",")

        if password == user[4]:
            return user
    
    return False

def newBalance_Deposit(user):
    f = open("5082557838" + ".txt", "w")
    user[5] = view_account_balance_deposit
    f.write(view_account_balance_deposit)
    f.close()

def newBalance_Withdrawal(user):
    f = open("5082557838" + ".txt", "w")
    user[5] = view_account_balance_withdrawal
    f.write(view_account_balance_withdrawal)
    f.close()

def authentication_file():
    f = open(auth_db_path + "current_session.txt", "w")
    f.write("User is logged in")


def remove_authentication_file():
    if os.path.exists(auth_db_path + "current_session.txt"):
        os.remove(auth_db_path + "current_login_session.txt")
    else:
        print("User not authenticated.")






#print(create(6702958901,["Tonessa", "Chatten", "tvchatten@gmail.com", "pythonista",300]))

#print(does_account_number_exist(6078542319))
#6078542319
#print(read({"One":"Two"}))
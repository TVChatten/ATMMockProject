def accountNumberValidation(accountNumber):

    # check if accountNumber is not empty

    # if accountNumber is 10 digits

    # if accountNumber is an integer

    if accountNumber: 

        try:
            
            int(accountNumber)

            if len(str(accountNumber)) == 10:
                return True

            else:
                print("Account Number cannot be less or more than 10 digits.")
                return False
        except ValueError:

            return False

        except TypeError:

            return False
    else:
        return False
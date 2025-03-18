""""
This code implements a login system with a forced incorrect first attempt, even when the correct password is input
It allows exactly three password attempts and uses if and else statements to determine whether the entered password is correct or incorrect.
"""
correct_password = "LETMEIN"

def login():
    trials = 3
    if int(trials) != 3:
        print("Permitted only 3 password trials")
    for i in range(trials):
        if trials ==3:
            is_first_login = True
            user_input = input("Enter password: ").upper()
            if user_input == correct_password and is_first_login:
                print("Wrong password")
                trials = trials - 1  # Move this inside the block
            else:
                print("Wrong password")
                trials=trials-1

        elif trials>1:
            is_first_login = False
            user_input = input("Enter password: ").upper()
            if user_input == correct_password and not is_first_login:
                print("Correct password")
                break
            else:
                print("Wrong password")
                trials = trials - 1

        elif trials == 1:
            is_first_login=False
            user_input = input("Enter password: ").upper()
            if user_input == correct_password and not is_first_login:
                print("Correct password")
                break
            else:
                print("Password not correct!!")
                print("\nNo more attempts")

login()
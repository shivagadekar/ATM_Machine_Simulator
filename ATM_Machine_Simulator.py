# ===============================***({ATM_MACHINE_UPDATE_V03})***==========================================
# In this update, all Main menu's are defined under defined_functions, with their names
# This also includes, Resend OTP feature.
# Comparatively, Code is much easier to read and modify
# In next version,
# 1.    We'll try to add feature to View/add/update user data
# 2.    Personnel information and ATM pin will be accessed with the help of CARD No only
# 3.    Code will be able to access information of number of people, without hesitating
# 4.    Ms-Excel may be used to store and access data
# 5.    If statement asking for "is Card inserted", if Yes - Then Executed all code or Try again popup
# 6.    Another Information regarding Update will be updated soon


import time as t

saving_account_balance = [200000]
current_account_balance = [200000]
atm_pin = [1234]
done = False


def card_insert_request():
    return print('Please Insert Your Card!')


def card_detect_msg():
    return print('Card Detected. Please Wait Some Time for Machine To Read Card !')


def greeting_msg():
    return print('Hello, Mr. Shivam Gadekar')


def main_menu():
    print('\nPlease Enter Number from Below List\n')
    # Check which operation user wants to perform
    print('1. Cash Withdraw \t\t\t\t\t'  # To withdraw cash from Account
          '2. Fast Cash Withdraw \t\t'  # To withdraw, without extra steps(fast)
          '3. View Account Balance \n'  # To View Current Account Balance
          '4. Account Transition Details \t\t'  # To view History
          '5. Reset Pin \t\t\t\t'
          '6. Quit Your Account \n')  # To reset pin


def cash_withdraw():
    # from which account, you want to withdraw money(saving or Current)
    print('Choose Account Type \n1. Saving \t\t\t\t\t\t\t2. Current')
    sub_choice = int(input('Your Choice : '))
    if sub_choice == 1:
        amount_to_withdraw = int(input('Enter Amount to withdraw in x $100 = '))
        if amount_to_withdraw < saving_account_balance[0]:
            var1 = amount_to_withdraw % 100
            if var1 == 0:
                t.sleep(2)
                print('Collect Your Cash. Mr. Shivam')
                user_choice = int(input('You want to view Account Balance : '
                                        '1. Yes                   2. No'))
                if user_choice == 1:
                    saving_account_balance[0] = saving_account_balance[0] - amount_to_withdraw
                    print('Your Account Balance is', saving_account_balance[0], 'Dollers.')
                elif user_choice == 2:
                    print('Thank You.')
            else:
                print('Enter Amounts in 100')
        else:
            print('Insufficient Account Balance.')
    elif sub_choice == 2:
        amount_to_withdraw = int(input('Enter Amount to withdraw in x $100'))
        if amount_to_withdraw < current_account_balance[0]:
            var1 = amount_to_withdraw % 100
            if var1 == 0:
                t.sleep(2)
                print('Collect Your Cash. Mr. Shivam')
                user_choice = int(input('You want to view Account Balance : '
                                        '1. Yes                   2. No'))
                if user_choice == 1:
                    current_account_balance[0] = current_account_balance[0] - amount_to_withdraw
                    print('Your Account Balance is', current_account_balance[0], 'Dollers.')
                else:
                    print('Thank You.')
            else:
                print('Enter Amounts in 100')
        else:
            print('Insufficient Account Balance.')


def fast_cash_withdraw():
    choice3 = int(input('Please Choose Amount 1. 1000 2. 2000 3. Enter Your Amount'
                        'Note : Amount will be Deduced from Saving Account'))
    if saving_account_balance[0] > 2000:
        if choice3 == 1:
            print('Collect Your Cash')
            saving_account_balance[0] = saving_account_balance[0] - 1000
        elif choice3 == 2:
            print('Collect Your Cash')
            saving_account_balance[0] = saving_account_balance[0] - 2000
        elif choice3 == 3:
            amount_to_withdraw = int(input('Enter Amount to withdraw in x $100'))
            if amount_to_withdraw < saving_account_balance[0]:
                if amount_to_withdraw == (amount_to_withdraw % 100 == 0):
                    print('Collect Your Cash. Mr. Shivam')
                    saving_account_balance[0] = saving_account_balance[0] - amount_to_withdraw
                else:
                    print('Enter Amounts in 100')
            else:
                print('Insufficient Account Balance.')


def view_account_bal():
    choice4 = int(input('Choose Account Type :\n1. Saving \2. Current'))
    if choice4 == 1:
        print('Your Saving Account Balance is : ', saving_account_balance[0], 'Dollers')
    elif choice4 == 2:
        print('Your Current Account Balance is : ', current_account_balance[0], 'Dollers')
    else:
        print('Oops. Wrong Choice')


def view_trans_details():
    t.sleep(2)
    print("You Don't Have Any Transition Details, We'll Do it Later, to Record History")


def reset_pin():
    print('Enter Your Phone Number +91-********81')
    mobile_no = int(input('Enter Your Phone No : '))
    if mobile_no == 9860645981:
        attempt1 = 3
        t.sleep(2)
        otp_conf = input('Received OTP 1.\t\tYes\t\t\t\t\t\t2.\t\tNo and Resend\n')
        if otp_conf == '1':
            otp = int(input('OTP is sent to Registered Mobile No,Please Enter = '))
            while attempt1 > 0:
                if otp == 1234:
                    new_pin = int(input('Enter New Pin : '))
                    atm_pin[0] = new_pin
                    break
                else:
                    print('Wrong OTP')
                    attempt1 -= 1
        elif otp_conf == "2":
            print('Oops! Technical Problem. Please Try After Some Time')
    else:
        print('Wrong Mobile Number, Enter Correct Phone Number.')


while not done:
    card_insert_request()
    t.sleep(1)
    card_detect_msg()
    t.sleep(2)
    greeting_msg()
    done2 = False
    attempt = 3
    while not done2:
        if attempt != 0:
            t.sleep(1)
            pin = int(input('Enter Your Four Digit Pin : '))
            if pin == atm_pin[0]:
                saving_account_balance[0] = saving_account_balance[0]
                current_account_balance[0] = current_account_balance[0]
                t.sleep(2)
                main_menu()
                choice = int(input('Enter Your Choice : '))
                if choice == 1:
                    cash_withdraw()
                if choice == 2:
                    fast_cash_withdraw()
                if choice == 3:
                    view_account_bal()
                if choice == 4:
                    view_trans_details()
                if choice == 5:
                    reset_pin()
                if choice == 6:
                    done = True
                    break
            else:
                if attempt == 1:
                    t.sleep(2)
                    print('Your Card is Blocked, Contact Bank.')
                    done2 = True
                attempt -= 1
                print('You Entered Wrong Choice, Only', attempt, 'Left.')
        else:
            print('You Entered Wrong OTP Too many Times.')
            done2 = True
# Paste this 'done = True' below done2, or your machine will work continuously Asking Please Insert Card!

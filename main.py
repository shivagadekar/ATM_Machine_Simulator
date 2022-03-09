# TODO: Add json file format for saving user data on server
# TODO: Convert This program into Function Programming
# TODO: Remove Bugs that occurred while testing on local machine
# TODO: Add GUI to this program using Tkinter
# TODO: The app should look exact copy of real ATM Machine for Study Purpose Only and Practicing
# TODO: Study Current Code as 5 months passed, after third revision of this file
# TODO: Have Brainstorming session with self and use ATM for understanding more functions of ATM
# TODO: Add two new features that you thing All ATM machines should have


import time as t

# Convert below portion into .json file and read data directly from json file.
# Json file should include: 
"""
Account_number: {
    account_no: 12312312313,
    account_type: 'saving/current'
    branch: BARB,
    branch_address: 
    ifsc: BARB000000,
    uidai: 123412341234,
    mobile_no: 8888888888,
    email: 'rajaram@gmail.com',
    fname: "Raj",
    mname: "Ramesh",
    sname: "Rampal",
    acc_balance: 132156465413513.054,
    dob: "20/12/1999",
    pan: "QWER123QER",
    occupation: "Student",
    address: "Mumbai-412321",
    nominee_added: "yes",
    ac_open_date: 12/12/2012,
    blood_group: "a-",
    history:{
        dd_mm_yyyy_hh_mm_ss:{
            transition_id: 132132323213563513,
            added: 13213,
            withdrawn: 1231,
        }
    },
    cards_allotaed: {
        credit:{
            credit_card_type: "platinum",
            credit_card_no: 1323213,
            name_on_card: "raj ramesh rampal",
            card_limit: 20000,
            amount_used: 10000,
            due_amount: 0000.0,
            card_issue_date: 12/12/2012,
            card_exp_date: 11/12/2025,
            cvv: 123123,
            credit_card_password: 1234,
            monthly_emi: 4225,
            history:{
                dd_mm_yyyy_hh_mm_ss:{
                    transition_id: 132132323213563513,
                    added: 13213,
                    withdrawn: 1231,
                }
            }
        },
        debit:{
            debit_card_type: "visa",
            debit_card_no: 1323213,
            name_on_card: "raj ramesh rampal",
            debit_limit_daily: 20000,
            card_issue_date: 12/12/2012,
            card_exp_date: 11/12/2025,
            cvv: 123123,
            debit_card_password: 1234,
            history:{
                dd_mm_yyyy_hh_mm_ss:{
                    transition_id: 132132323213563513,
                    added: 13213,
                    withdrawn: 1231,
                }
            },            
        }
    } 
}    
"""
saving_account_balance = [200000]
current_account_balance = [200000]
atm_pin = [1234]
done = False


def card_insert_request():
    return print('Please Insert Your Card!')


def card_detect_msg():
    """ For this code, enter last four digit of card + phone No"""
    return print('Card Detected. Please Wait Some Time for Machine To Read Card !')


def greeting_msg():
    "Take name of user from json file and show in this greeting message"
    return print('Hello, Mr. Shivam Gadekar')


def main_menu():
    """
    Initially work on menus of this windows.
    First Screen Should be 
        1. Select Account Type
            1.1 Saving
                1.1.1 Withdraw
                1.1.2 Fast Withdraw
            1.2 Current ... Add remaining Options and save in variable
    """
    print('\nPlease Enter Number from Below List\n')
    # Check which operation user wants to perform
    print('1. Cash Withdraw \t\t\t\t\t'  # To withdraw cash from Account
          '2. Fast Cash Withdraw \t\t'  # To withdraw, without extra steps(fast)
          '3. View Account Balance \n'  # To View Current Account Balance
          '4. Account Transition Details \t\t'  # To view History
          '5. Reset Pin \t\t\t\t'
          '6. Quit Your Account \n')  # To reset pin


def cash_withdraw():
    """Use password and account balance from json to verify is user capable of withdrawing that amount 
    of money. If yes then deduct that much amount of money from account."""
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
    """Use password and account balance from json to verify is user capable of withdrawing that amount 
    of money. If yes then deduct that much amount of money from account.
    show 6 fast withdraw money option."""

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
    """Use password and account balance from json and then show account balance."""
    choice4 = int(input('Choose Account Type :\n1. Saving \2. Current'))
    if choice4 == 1:
        print('Your Saving Account Balance is : ', saving_account_balance[0], 'Dollers')
    elif choice4 == 2:
        print('Your Current Account Balance is : ', current_account_balance[0], 'Dollers')
    else:
        print('Oops. Wrong Choice')


def view_trans_details():
    """Use password and account balance from json and show last transition details."""
    t.sleep(2)
    print("You Don't Have Any Transition Details, We'll Do it Later, to Record History")


def reset_pin():
    """Use password and account balance from json to verify uidai, enter phone no and receive otp and enter
    that otp in that file."""
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
    """Run all functions as per requirement."""
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

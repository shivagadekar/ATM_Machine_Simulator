# Successfully Uploaded
# I have made this this changes in this File, After closing browser.
# This Programme is To Simulate Basic ATM Machine Operations.
# As I Become professional, we'll upgrade this code accordingly.
print('Please Insert Your Card!')
print('Hello, Mr. Shivam Gadekar')
atm_pin = 1234
attempt = 3  # Initial attempts to enter pin, allot 3 attempts, after 3 wrong attempts Card will be blocked
while attempt > 0:
    # Take input from user, that is 4 Digit ATM Pin
    pin = int(input('Enter Your Four Digit Pin : '))
    if pin == atm_pin:
        saving_account_balance = 165812
        current_account_balance = 188027
        print('Please Enter Number from Below List')
        # Check which operation user wants to perform
        print('1. Cash Withdraw '  # To withdraw cash from Account
              '2. Fast Cash Withdraw '  # To withdraw, without extra steps(fast)
              '3. View Account Balance '  # To View Current Account Balance
              '4. Account Transition Details '  # To view History
              '5. Reset Pin')  # To reset pin
        choice = int(input('Enter Your Choice : '))
        if choice == 1:
            # from which account, you want to withdraw money(saving or Current)
            print('Choose Account Type \n1. Saving \t \t2. Current')
            sub_choice = int(input('Your Choice = '))
            if sub_choice == 1:
                amount_to_withdraw = int(input('Enter Amount to withdraw in x $100 = '))
                if amount_to_withdraw < saving_account_balance:
                    var1 = amount_to_withdraw % 100
                    if var1 == 0:
                        print('Collect Your Cash. Mr. Shivam')
                    else:
                        print('Enter Amounts in 100')
                        break
                else:
                    print('Insufficient Account Balance.')
                    break
            elif sub_choice == 2:
                amount_to_withdraw = int(input('Enter Amount to withdraw in x $100'))
                if amount_to_withdraw < current_account_balance:
                    var1 = amount_to_withdraw % 100
                    if amount_to_withdraw == (var1 != 0):
                        print('Collect Your Cash. Mr. Shivam')
                        break
                    else:
                        print('Enter Amounts in 100')
                        break
                else:
                    print('Insufficient Account Balance.')
                    break
        if choice == 2:  # Fewer Step Withdraw
            choice = int(input('Please Choose Amount 1. 1000 2. 2000 3. Enter Your Amount'
                               'Note : Amount will be Deduced from Saving Account'))
            if saving_account_balance > 2000:
                if choice == 1:
                    print('Collect Your Cash')
                    saving_account_balance = saving_account_balance - 1000
                elif choice == 2:
                    print('Collect Your Cash')
                    saving_account_balance = saving_account_balance - 2000
                elif choice == 3:
                    amount_to_withdraw = int(input('Enter Amount to withdraw in x $100'))
                    if amount_to_withdraw < saving_account_balance:
                        if amount_to_withdraw == (amount_to_withdraw % 100 == 0):
                            print('Collect Your Cash. Mr. Shivam')
                            saving_account_balance = saving_account_balance - amount_to_withdraw
                        else:
                            print('Enter Amounts in 100')
                    else:
                        print('Insufficient Account Balance.')
                        break
        if choice == 3:
            choice = int(input('Choose Account Type :\n1. Saving \2. Current'))
            if choice == 1:
                print('Your Saving Account Balance is : ', saving_account_balance, 'Dollers')
            elif choice == 2:
                print('Your Current Account Balance is : ', current_account_balance, 'Dollers')
            else:
                print('Oops. Wrong Choice')
        if choice == 4:
            print("You Don't Have Any Transition Details, We'll Do it Later, to Record History")
        if choice == 5:
            print('Enter Your Phone Number +91-********81')
            mobile_no = int(input('Enter Your Phone No : '))
            if mobile_no == 9860645981:
                attempt = 3
                otp = int(input('OTP is sent to Registered Mobile No,Please Enter = '))
                while attempt > 0:
                    if otp == 1234:
                        new_pin = int(input('Enter New Pin : '))
                        atm_pin = new_pin
                        break
                    else:
                        print('Wrong OTP')
                        attempt -= 1
            else:
                print('Your Card is Blocked, Contact Bank For More Details.')
    else:
        attempt -= 1
        if attempt == 0:
            print('Your Card is Blocked, Contact Bank.')
        print('You Entered Wrong Choice, Only', attempt, 'Left.')

dict = {'usrnm':None, 'psswrd':None}



#Initial question:
IntQ = input("""
What would you like to do?
\nFor New Username and Password, type \"New_User\"
\nTo Logout, type \"Logout\"

>>> """)

for runner in IntQ:
    while IntQ.lower() not in {'new_user', 'logout'}:
        IntQ = input('Please enter a valid option... ')
        IntQ = IntQ
    for ans in IntQ:
        if IntQ.lower() == "logout":
            print("""

            Have a nice day!

            """)
            exit()

        if IntQ.lower() == "new_user":
            Nuser = input("Enter a new User_Name: ")
            dict['usrnm'] = (Nuser)
            print("User_name Confirmed")
            Npass = input("Enter a new Password: ")
            dict['psswrd'] = (Npass)
            print("Password confirmed")
            pass_cnvrt = '*' * len(Npass)
            print(f"""

            Setup completed \"{Nuser}\", your password,\"{pass_cnvrt}\"
            is {len(pass_cnvrt)} characters long.
            """)
            break
    IntQ = input(f"""

    \nWelcome back, \"{Nuser}\"... what would you like to do now?

    \nTo Logout, type \"Logout\"

    >>> """)
    for runner in IntQ:
        while IntQ != "logout":
            IntQ = input("Please enter a valid option... ")
            IntQ = IntQ
        for ans in IntQ:
            if IntQ.lower() == "logout":
                print(f"""

                Have a wonderful day {Nuser}! Until next time!
                ----------------------------------------------
                Dictionary statistics:
                Username: {dict['usrnm']}
                Password: {dict['psswrd']}
                """)

                exit()

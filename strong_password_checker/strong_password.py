import re

print("Welcome to Strong Password checker!!!")

# Create password complexity requirments using regular expression
password_regex = re.compile(r'''(
    ^(?=.*[A-Z].*[A-Z])                # at least 2 capital letters
    (?=.*[!@#($&%+)*])                 # at least 1 of these special characters
    (?=.*[0-9].*[0-9].*[0-9])          # at least 3 numeric digits
    (?=.*[a-z].*[a-z])                 # at least 2 lower case letters
    .{8,}                              # at least 8 total digits
    $
    )''', re.VERBOSE)


def password_check():
    # Ask user for password
    user_pass = input("Enter a potential password: ")

    # Check complexity of the password
    mo = password_regex.search(user_pass)

    if (not mo):
        print("This is not a strong password! Please come up with a stronger password.")
        return False

    else:
        print("Your given password meets the strong password complexity requirements!")
        print("Checking weak password from database...")

        # Open the list of password database
        pass_list = open("password_list.txt", 'r')
        is_in = False
        i = 0 

        # Check each password of password_list database
        for line in pass_list:
            i += 1
            if user_pass in line:
                is_in = True
                print("Your password was found in weak password database! Please come up with a strong password.")
                break
        else:
            print("Your password was not found in weak password database.")
            print("YOUR PASSWORD IS STRONG!!!")
        

password_check()
user_name = "kudi"

password = '12345wk'

failed_limit = 3

start_login = 0

while start_login < failed_limit:

    user_name = input("\nenter your user name: ".title())
    password = input("enter your user password: ".title())
    #password = int(password)

    if user_name == "kudi" and password == '12345wk':

        welcome_message = f"welcome, {user_name}".title()

        print(welcome_message)

        print("you have logged in successfully!".title())

        break

    else:

        print("Invalid username or password")

        start_login += 1

print(f"\nYou have tried {start_login} times and failed!")

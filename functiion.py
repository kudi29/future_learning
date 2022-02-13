def test_function(user_name='', password=''):

    user_name = input("enter your user name: ".title())

    password = input("enter your user password: ".title())

    password = int(password)

    if user_name == 'kudi' and password == 12345:

        user_message = f"welcome, {user_name}".title()

        print("you have logged in successfully!".title())

        return user_message

    else:
        print("Invalid username or password")


user_data = test_function()

print(user_data)

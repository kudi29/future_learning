to_do_list = []

prompt = "Enter 'quit' to quit"
prompt += "\nEnter a list of things u do when you wakes up: "

user_data = True

while user_data:

    to_do = input(prompt.title())

    if to_do == 'quit':

        break

    to_do_list.append(to_do)

    print(to_do_list)

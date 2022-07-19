restart = "yes"
while restart == "yes":

    import string
    import random

    characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

    def generate_basic_random_password():
        length = int(input("Enter password length: "))

        random.shuffle(characters)

        password = []
        for i in range(length):
            password.append(random.choice(characters))   # picking random characters from the list

        random.shuffle(password)   #shuffling the chosen password

        print("".join(password))    #Converting list to string and printing the list


    generate_basic_random_password()  ## starting the function
    restart = input("do you want to restart? \nyes or no?")
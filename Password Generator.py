import string
import random
chars = list(string.ascii_letters)
nums = list(string.digits)
specialchars = """[];'#,./{}:@~<>?!"£$%^&*()"""

def Password_Generator():
    char = int(input("How many characters do you want?"))
    num = int(input("How many numbers do you want?"))
    specialchar = int(input("How many special characters do you want?"))

    length = char + num + specialchar

    password = []
    for i in range(char):
            password.append(random.choice(chars))
    for i in range(num):
        password.append(random.choice(nums))
    for i in range(specialchar):
        password.append(random.choice(specialchars))

        random.shuffle(password)
        print("".join(password))

Password_Generator()



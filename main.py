#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Level_1 = Example-- should be like We29(#

# password = ""
# for p in range(1, nr_letters + 1):
#  random_letters = random.choice(letters)
#  password += random_letters

# password2 = ""
# for p in range(1, nr_numbers + 1):
#  random_numbers = random.choice(numbers)
#  password2 += random_numbers

# password3 = ""
# for p in range(1, nr_symbols + 1):
#  random_symbols = random.choice(symbols)
#  password3 += random_symbols

# print(password + password3 + password2)

#Level_2 = Should be like fd6&uh783y#774@#

password_list = []
for p in range(1, nr_letters + 1):
    password_list += random.choice(letters)


for p in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)


for p in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

random.shuffle(password_list)

Password = ""
for char in password_list:
  Password += char
print(f"Your Password is: {Password}")  


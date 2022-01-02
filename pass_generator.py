# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

pass1 = ''

for letter in range(0, nr_letters):
    random_letters = random.choice(letters)
    pass1 += random_letters

for symbol in range(0, nr_symbols):
    random_symbols = random.choice(symbols)
    pass1 += random_symbols

for number in range(0, nr_numbers):
    random_numbers = random.choice(numbers)
    pass1 += random_numbers

print(f"Easy pass: {pass1}")


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

split_pass = []
for item in pass1:
    split_pass.append(item)

random.shuffle(split_pass)

hard_pass = ''.join(split_pass)

print(f"Hard pass: {hard_pass}")

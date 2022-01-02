# exercise find max number withowt max() function

user_input = input("Enter hights: ").split()

numbers_list = []

for item in user_input:
    numbers_list.append(int(item))

print(numbers_list)

highest_number = 0
for item in numbers_list:
    if item > highest_number:
        highest_number = item

print(f"The biggest number is: {highest_number}")

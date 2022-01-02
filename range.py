for number in range(1, 11):
    print(number)  # 11 is not included

for number in range(1, 11, 2):  # increase by 2
    print(number)  # 1 3 5 7 9


total = 0
for number in range(1, 101):
    total += number

print(total)

# exercise calculate sum of even numbers from 1 to 100

my_sum = 0

for number in range(1, 101):
    if number % 2 == 0:
        my_sum += number

print(my_sum)

# OR

total = 0

for number in range(2, 101, 2):
    total += number

print(total)

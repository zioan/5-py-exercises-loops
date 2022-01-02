fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)


# exercise - calculate average
# use NO len() and NO sum()
user_input = input("Enter the numbers:").split()

my_list = []

for item in user_input:
    my_list.append(int(item))

my_sum = sum(my_list)


sum = 0
count = 0

for item in my_list:
    sum += item
    count += 1

average = sum / count

print(average)

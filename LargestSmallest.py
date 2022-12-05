condition = input("Do you want to enter a number ")

largest_number = float("-inf")
smallest_number = float("inf")

while condition != "end":
    number = int(input("enter a number : "))
    if number > largest_number:
        largest_number = number

    if number < smallest_number:
        smallest_number = number

    condition = input("Do you want to enter a number ")

print(largest_number)
print(smallest_number)

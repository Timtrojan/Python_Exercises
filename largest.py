largest_number_so_far = 0

second_largest_number_so_far = 1
loop = 0
while loop < 5:
    number = int(input("input a number : "))
    loop += 1
    if number > largest_number_so_far:
        largest_number_so_far = number

    if number < smallest_number_so_far:
        smallest_number_so_far=number

    if number
print("the largest number is", largest_number_so_far)
print("the smallest number is", smallest_number_so_far)


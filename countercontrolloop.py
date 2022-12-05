count = 0
largest_number_so_far = -float(inf)
smallest_number_so_far =

while count < 2:
    num = int(input("Give me a number : "))
    if num > largest_number_so_far:
        largest_number_so_far = num

    if smallest_number_so_far < num:
        smallest_number_so_far = num
    count += 1
print("the largest number is", largest_number_so_far)
print("the smallest number is", smallest_number_so_far)

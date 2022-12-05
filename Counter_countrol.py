input_values = int(input("Enter a number: "))

input_sum = 0
count = 0
positive_count = 0
negative_count = 0
while input_values != 0:
    input_values = int(input("Enter a number: "))
    if input_values < 0:
        negative_count += 1
    else:
        positive_count += 1

    count += 1
    input_sum = input_sum + input_values

print("The number of positives is ", positive_count)
print("The number of negative numbers is", negative_count)
print("The total is", input_sum)
print("The average is", input_sum / count)

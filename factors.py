number = int(input("Enter a number to get factors : "))
count1 = 1
sum_factors = 0

while count1 < number:
    factors_count = number % count1
    if factors_count == 0:
        sum_factors += count1

    count1 += 1

if sum_factors < number:
    print(number, "is deficient")
elif sum_factors > number:
    print(number, "is abundant")
else:
    print(number, "is perfect")

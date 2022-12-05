letter = "Hello There!!!"
print(letter.count("e"))
print(letter.upper())
print(letter.lower())
print(letter.capitalize())
print(letter.title())
print(letter.casefold())
print(letter.swapcase())

print(letter.center(20, "*"))
print(letter.endswith("!"))
print(letter.replace("l", "r", 3))
print(letter.split("e"))
print(letter.partition("e"))
print("-".join(["e", "b"]))

bin_ = "101010101010101010111078"

print(bin_.replace("1", "x").replace("0", "1").replace("x","0"))
print(bin_.translate(str.maketrans("01","10")))
print(bin_.translate(str.maketrans("01","10","8")))

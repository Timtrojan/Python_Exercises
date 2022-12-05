s = "hello world"
to_be_found = "e"
for index, char in enumerate(s):
    if char == to_be_found:
        print(f"{char}found at {index}")
        break
else:
    print(-1)

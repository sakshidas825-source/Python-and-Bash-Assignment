text = input("Enter some text: ")

with open("sample.txt", "w") as file:
    file.write(text)

print("Text written to sample.txt")
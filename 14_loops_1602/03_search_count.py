string = 'Hello, world! I am a Python developer!'

for i in range(len(string)):
    if string[i].isalpha():
        print(f"Letter: «{string[i]}»")
    else:
        print(f"Punctuation: «{string[i]}»")



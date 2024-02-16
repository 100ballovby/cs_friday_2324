"""
Существуют методы проверки регистра
и методы проверки того, с чего начинается строка:

- islower()
- isupper()
- startwith()
- endswidth()
"""
l = ['F', 'f', 'hello', 'homework']

for i in range(len(l)):
    print(f'{l[i]} is big letter {l[i].isupper()}')
    print(f'{l[i]} is small letter {l[i].islower()}')
    print(f'{l[i]} starts with "hell" {l[i].startswith("hell")}')
    print(f'{l[i]} ends with "work" {l[i].endswith("work")}')



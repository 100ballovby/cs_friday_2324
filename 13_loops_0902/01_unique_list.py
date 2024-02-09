import random 


a = []
while (len(a) < 10):
    n = random.randint(0, 50)
    if n not in a:
        a.append(n)

print(a)

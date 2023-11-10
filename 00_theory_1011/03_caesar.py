msg = input('Message: ')
shift = int(input('Shift: '))
encrypted = ''

for i in range(len(msg)):
    symbol = msg[i]  # сохраняю каждую букву в отдельной переменной
    if symbol.isalpha():  # если символ - это буква
        if symbol.islower():  # если я работаю с маленькой буквой
            shifted = chr((ord(symbol) - ord('a') + shift) % 26 + ord('a'))
        else:  # если я работаю с большой буквой
            shifted = chr((ord(symbol) - ord('A') + shift) % 26 + ord('A'))
        encrypted += shifted  # добавляю сдвинутую букву в результат
    else:  # если символ буквой не является
        encrypted += symbol  # записываем без изменений

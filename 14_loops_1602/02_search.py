# Линейный поиск в строке
phrase = input('Phrase: ')
symbol = input('Symbol: ')


for i in range(len(phrase)):
    if phrase[i] == symbol:
        print(f'Found, index: {i}')
        break


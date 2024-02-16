symbols = ['a', '3', '!', '®', '\0']

for i in range(len(symbols)):
    print(f'{symbols[i]} is letter {symbols[i].isalpha()}')
    print(f'{symbols[i]} is number {symbols[i].isdigit()}')
    print(f'{symbols[i]} is printable {symbols[i].isprintable()}')
    print(f'{symbols[i]} is ascii {symbols[i].isascii()}')
    print(f'{symbols[i]} is space {symbols[i].isspace()}')

"""
Все вышеуказанные методы являются методами проверки строки.
Это значит, что, если проверка проходит, то методы
возвращают True. Если проверка не проходит, то методы
возваращют False. Это значит:
если symbols[i] является буквой, то примененный метод
.isalpha(), который проверяет, что символ является символом
алфавита, вернет True. Если бы symbols[i] был цифрой или чем-то другим,
то метод .isalpha() вернул бы False.
"""


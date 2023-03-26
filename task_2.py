#Задание №2

#Дано слово из маленьких латинских букв. Сколько там согласных и гласных букв? Гласными называют буквы «a», «e», «i», «o», «u».

#Для решения задачи создайте переменную и в неё положите слово с помощью input()

#А также определите количество каждой из этих гласных букв Если какой-то из перечисленных букв нет - Выведите False

#count
string = input('Введите слова маленькими буквами: ')
a = string.count ('a')
e = string.count ('e')
i = string.count ('i')
o = string.count ('o')
u = string.count ('u')

f = 'False'
if a == 0:
    print(f'a - {f} ')
if e == 0:
    print(f'e - {f}' )
if i == 0:
    print(f'i - {f} ')
if o == 0:
    print(f'o - {f} ')
if u == 0:
    print(f'u - {f} ')
print(f'Гласных: {a + e + i + o + u}')
print(f'Согласных: {len(string) - (a + e + i + o + u)}')

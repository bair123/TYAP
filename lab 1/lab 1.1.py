import random


rand = random.randint(0, 10)
a = True
while a:
    chislo = int(input('Введите число: '))
    if rand == chislo:
        print('Поздравляем! Вы Выиграли!')
        a = False
    else:
        if chislo < rand:
            print('Ваше число меньше!')
        else:
            print('Ваше число больше!')

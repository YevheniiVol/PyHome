a = int(input('Введите элемент в виде целого числа А: '))
b = int(input('Введите элемент в виде целого числа Б: '))
c = int(input('Введите элемент в виде целого числа В: '))

if a > b:
        print('Свершилось!')
elif b > a:
        print('Да ну!')
else:
    if a == b:
             print('А если так?')
             a = a+c
             b = b-c
             if a > b:
                 print('Свершилось!')
             elif b > a:
                 print('Да ну!')

def z41():
    a = int(input('Введите число '))
    b = a % 3
    if b == 0:
        print('Число делится на три')
    else:
        print('Число не делится на три')

def z42():
    try:
        a = int(input('Введите число  '))
        b = a % 100
    except ValueError:
        print('Введено не число!')
    else:
        if b == 0:
            print('Число делится на 100')
        elif a == 0:
            print('Введен ноль!')
        else:
            print('Число не делится на 100')

def z43():
    date = input("введите дату в формате дд.мм.гггг: ")
    date = date.split('.')
    if int(date[0]) * int(date[1]) == int(date[2][2:4]):
        print("поздравляю, дата магическая")
    else:
        print("дата не магическая")

def z44():
    ticket = input("введите номер билета: ")
    chet1 = 0
    chet2 = 0
    if len(ticket) % 2 == 0:
        for i in ticket[0:int(len(ticket) / 2)]:
            chet1 = chet1 + int(i)
        for i in ticket[int(len(ticket) / 2):int(len(ticket)) + 1]:
            chet2 = chet2 + int(i)
        if chet1 == chet2:
            print("счастливый билет")
        else:
            print("билет не счастливый")
    else:
        print("количество цифр нечётно, купите новый билет")

#z41(), z42(), z43(), z44()


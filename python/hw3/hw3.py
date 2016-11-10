list = []
for i in range(7):
    list.append(int(input('Введите число: ',)))
for i in range(7):
    if list[i] > 0:
        print(list[i] * 'X')
    else:
        print()
        

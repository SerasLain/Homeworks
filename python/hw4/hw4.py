a = list(input('Введите слово: ',))
for i in range(len(a)):
    print(*a[i:], sep = '')

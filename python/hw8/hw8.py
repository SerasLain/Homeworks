import random
def openfile():
    with open('dictionary.csv', 'r', encoding = 'utf-8') as f:
        file = f.readlines()
        dictionary = {}
        for line in file:
            string = line.split(', ')
            string[1] = string[1].strip()
            dictionary[string[0]] = string[1]
        return dictionary
def guess():
    dictionary = openfile()
    arr = sorted(dictionary.keys())
    word = str(random.choice(arr))
    p = dictionary[word]
    print('Загадала! Подсказка: '+p)
    i = 3
    while i != 0:
        i-=1
        t = input('Слово: ')
        if t == word:
            print('Верно!')
            break
        else:
            if i == 0:
                print('Не угадал, это было слово '+word)
                break
            t = print('Неправильно! Попыток у тебя еще '+str(i))
def main():
    guess()
    a = input('Сыграем еще?\n')
    if a == ('да' or 'ага'):
        main()
    else:
        print('Ну и ладно. Пока')
main()

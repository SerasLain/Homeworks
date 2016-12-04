score = 0
count = 0
with open ('text.txt', 'r', encoding='utf-8') as f:
    for line in f:
        string = line.split()
        count += len(string)
        for word in string:
            if word[0].istitle():
                    score +=1
if count == 0:
    print('Пустой файл( Нечего считать!')
else:
    total = score/count*100
    print('Процент слов с большой буквы: ', total, '%', sep ='')


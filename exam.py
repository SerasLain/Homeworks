a = 'союз'
b = 'сущ'
c = 'жен'
count = 0
femwords = []
words = []
with open ('D:/new1.txt', 'r', encoding='utf-8') as f:
    for line in f:
        string = line.split()
        if a == string[2]:
            print(line, sep =' ')
        ## второе задание
        if b and c in string:
            femwords.append(string[0])
            num = float(string[-1])
            count +=num
print(count, femwords, sep=', ')
## третье задание
while input()!='':
    words.append(input())
    for line in f:
        string = line.split()
        for i in range(len(words)):
            if words[i] == string[0]:
                print(string)
            else:
                break
                print('Слово не нашлось')

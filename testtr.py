import re

def readtext():
    with open(input('Введите путь к файлу: '), 'r', encoding = 'utf-8') as f:
        text = f.read()
    return text


##def writesmth(a):
##    with open(input('Введите путь к csv файлу: ', 'a', encoding = 'utf-8')) as fi:
##              fi.write(a)
##
def normaltext(text):
    ##обрезает у словоформ в массиве всякие знаки препинания, включая тире, сводит все
    ## словоформы к нижнему регистру и возвращает массив словоформ
    arr = []
    text = re.sub(r'—\s?', r' ', text)
    text = text.split()
    for i in range(len(text)):
        word = text[i].strip('.,?()"')
        arr.append(word.lower())
    return arr


def freqdict(text):
    ##Возвращает словарь, в котором ключи слова, а значения - их частотность в тексте
    freq = {}
    for i in text:
        n = text.count(i)
        freq[i] = n
    return freq

def delete_doubles(d):
    nd = {}
    a = sorted(d.keys())
    for key in a:
        if key not in nd.keys():
            nd[key] = d[key]
    return nd

def main():
    wordlist = normaltext(readtext())
    ## 1 задание. Открыть файл, посчитать словоформы
    countall = len(wordlist)
    print('Число слов', countall)
    ## 2 задание. Посчитать частотность словоформ, создать словарь "слово - частота", записать его в .csv
    fdict = delete_doubles(freqdict(wordlist))
    s = sorted(fdict.keys())
    file = open(input('Введите путь к csv файлу: '), 'a', encoding = 'utf-8')
    for word in s:
        file.write(word+','+str(fdict[word])+'\n')
    file.close()

## проблема с сортировкой

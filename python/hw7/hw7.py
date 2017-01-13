def normaltext(text):
    arr = []
    for i in range(len(text)):
        word = text[i].strip('.,?()"')
        arr.append(word.lower())
    return arr
def openfile():
    with open(input('Введите путь к файлу: '), 'r', encoding='utf-8') as f:
        text = f.read()
        text = text.split()
    return text
def findomni(text):
    ## ищет в тексте слова с приставкой омни- и возвращает найденное в виде списка 
    omniwords = []
    for i in range(len(text)):
        if len(text[i]) > 4:
            if text[i][:4] == 'omni':
                omniwords.append(text[i])
    return omniwords
def biteomni(omniwords):
    ## убирает приставку омни-
    words = []
    for i in range(len(omniwords)):
        words.append(omniwords[i].strip('omni'))
    return words
def unique(a):
    ## создает список, в котором слова не повторяются
    uniquearr = []
    for i in range(len(a)):
        if a[i] not in uniquearr:
            uniquearr.append(a[i])
    return uniquearr
def countfreq(words, text):
    ## считает частоту, с которой слова из первого списка встречаются во втором, 
    ## записывает результат в виде предложения в список
    q = len(text)
    uniqwords = unique(words)
    result = []
    for i in range(len(uniqwords)):
        a = words.count(uniqwords[i])
        if a != 0:
            result.append(uniqwords[i]+': частота в тексте - '+ str((a/q)*100) + '%')
        else:
            result.append(uniqwords[i]+' в тексте не встречается')
    return result
def sum_up(resultomni, resultwords):
    ## печатает элементы, чередуя списки
    for i in range(len(resultomni)):
        print(resultomni[i])
        print(resultwords[i])
def main():
    text = normaltext(openfile())
    omniwords = findomni(text)
    words = biteomni(omniwords)
    resultwords = countfreq(words, text)
    resultomni = countfreq(omniwords, text)
    sum_up(resultomni, resultwords)
main()    
    
        

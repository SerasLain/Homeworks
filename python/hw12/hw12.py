def opentext():
    f = open('testtr_text.txt', 'r', encoding='UTF-8')
    text = f.read()
    f.close()
    return text


def makesent(text): 
    ## расставляет символ-разделитель предложений
    text = text.replace('.','.*')
    text = text.replace('?', '?*')
    text = text.replace('!', '!*')
    return text


def sentencer(text):
    ## создает массив из предложений с сохранением всей пунктуации
    sentarr = [sentence for sentence in text.split('*')]
    return sentarr


def medlength(sentence):
    ##считает среднюю длину слов в предложении
    arr = [len(word.strip('./",:;-—()!?')) for word in sentence.split()]
    med = round(sum(arr)/len(sentence.split()), 1)
    return med


def dictsentlen(sentarr):
    ##создает словарь вида предложение: средняя длина слова в предложении для предложений длиннее десяти слов
    dictionary = {sentence: medlength(sentence) for sentence in sentarr if len(sentence.split()) > 10}
    return dictionary


def printsentml(dictionary):
    arr = [key+' '+'\nЭто предложение со словами длины {}'.format(dictionary[key]) for key in dictionary]
    for i in arr:
        print(i)


def main():
    printsentml(dictsentlen(sentencer(makesent(opentext()))))


if __name__ == "__main__":
    main()

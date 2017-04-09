<<<<<<< HEAD
def opentext():
    f = open('testtr_text.txt', 'r', encoding='UTF-8')
    text = f.read()
    f.close()
    return text


def makesent(text):
    text = text.replace('.','.*')
    text = text.replace('?', '?*')
    text = text.replace('!', '!*')
    return text


def sentencer(text):
    sentarr = [sentence for sentence in text.split('*')]
    return sentarr


def medlength(sentence):
    arr = [len(word.strip('./",:;-—()!?')) for word in sentence.split()]
    med = round(sum(arr)/len(sentence.split()), 1)
    return med


def dictsentlen(sentarr):
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
=======
import re
def openarticle():
    with open(input('Введите путь к файлу: '), 'r', encoding='utf-8') as f:
        text = f.read()
    return text


def writeorderlist(order):
    with open(input('Введите путь к файлу: '), 'a', encoding='utf-8') as f:
        f.write(order)

        
def findorder(text):
    regword = r'Отряд.*?>([\w]*)</a></td>'
    matched = re.search(regword, text, flags = re.DOTALL)
    order = matched.group(1)
    return order


def main():
    writeorderlist(findorder(openarticle()))

main()
>>>>>>> 7c434fbb0500b55f59da625d33f5a38e9b7043fd

import re


def readstrings():
    with open('Fil.xml', 'r', encoding = 'utf-8') as f:
        text = f.readlines()
    return text

def readtext():
    with open('Fil.xml', 'r', encoding = 'utf-8') as f:
        text = f.read()
    return text



def countstrings(text):
    num = len(text)
    return num


def opentowrite(num):
    with open('anotherfil.txt', 'w', encoding = 'utf-8') as f:
        f.write(num)


def dictionary():
    text = readtext()
    strings = readstrings()
    regword = r'type="(.*?)"'
    reglemma = r'<w lemma'
    dictionary = {}
    for line in strings:
        test = re.search(reglemma, line)
        if test != None:
            matched = re.search(regword, line)
            matchedword = r'"'+matched.group(1)+r'"'
            num = len(re.findall(matchedword, text))
            dictionary[matched.group(1)] = num
    return dictionary


def findaj(dictionary):
    regword = r'l.f.*'
    l = sorted(dictionary.keys())
    for typ in l:
        a = re.match(regword, typ)
        if a != None:
            with open('anfile.txt', 'a', encoding = 'utf-8') as f:
              f.write(typ+' '+str(dictionary[typ])+'\n')
        

def writekeys(dictionary):
    a = sorted(dictionary.keys())
    with open('Keys.txt', 'w', encoding = 'utf-8') as f:
        f.write('\n'.join(a))

## третье задание, часть два. Но уже поздно.
##    def clean(textstr):
##      regbody = r'body>(.*)<//bo'
##      body = re.search(textstr, regbody, flags = re.DOTALL)
##      body = body.group(1)
##      body.split('\n')
    ##разделить body на строки, из каждой строки вытащить то, что междду кавычками
    ##в соответствующих тегах в три переменные,
    ##собрать их в строку и сразу записать в файл.csv, открытый в режииме 'a'
    
    

def main():
    opentowrite(str(countstrings(readstrings()))) ##первое задание
    writekeys(dictionary()) ##второе задание
    findaj(dictionary()) ##номер три часть один

main()

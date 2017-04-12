import os
import re

def filesaround():
    ## возвращает список всех файлов в текущей папке
    arrnames = os.listdir('.')
    arrfiles = [name for name in arrnames if os.path.isfile(name) == True]
    return arrfiles


def eatextension(arrnames):
    ## возвращает на выходе словарь, где ключ - название файла, а значение - его расширение.
    ## как следствие - названия не повторяются
    noextnames = [re.search(r'(.*)\.(.*)', name) for name in arrnames]
    dictnames = {name.group(1): name.group(2) for name in noextnames}
    return dictnames


def fileswith(dictnames):
    ## возвращает список названий файлов, без повторов
    arrfileswith = [key for key in dictnames.keys() if re.search('[.,!_;]', key) != None]
    return arrfileswith


def main():
    for word in fileswith(eatextension(filesaround())):
        print(word)

main()

import os
import re

def filesaround():
    ## возвращает список всех файлов в текущей папке
    arrnames = os.listdir('.')
    arrfiles = [name for name in arrnames if os.path.isfile(name) == True]
    return arrfiles


def file_ext(arrfiles):
    ## возвращает массив с именами файлов, размеченными на название и расширение.
    ## а закомментирован словарь, который бы содержал название:расширение. Как следствие - названия не повторяются
    arrnames = [re.search(r'(.*)\.(.*)', name) for name in arrfiles]
    ## dictnames = {name.group(1): name.group(2) for name in noextnames}
    return arrnames


def fileswith(arrnames):
    ## возвращает список названий файлов со знаками препинания
    arrfileswith = [key.group(0) for key in arrnames if re.search('[.,!_;]', key.group(1)) != None]
    return arrfileswith

        
def exercize():
    allelementsindir = os.listdir('.')
    arrfiles = [name for name in allelementsindir if os.path.isfile(name) == True]
    arrfiles = file_ext(arrfiles)
    arrdirs = [name for name in allelementsindir if os.path.isdir(name) == True]
    filenames = [file.group(1) for file in arrfiles]
    unicarr = []
    for name in arrfiles:
        if name.group(1) not in unicarr:
            unicarr.append(name.group(1))
    for name in arrdirs:
        if name not in unicarr:
            unicarr.append(name)
    return unicarr

def main():
    ## 1. Надеюсь, я верно поняла задание, и тут надо с повторами и расширениями
    print('Это на первое задание')
    for word in fileswith(file_ext(filesaround())):
        print(word)
    ## 2. Названия всего без повторов
    print('А это на второе')
    for word in exercize():
        print(word)
main()

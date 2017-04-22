import os
import shutil
##os.listdir('..') ##На уровень выше
##tree = os.walk('.') ## ходит по папкам и все собирает
###возвращает generator - типа массив. Можно распечатать в цикле. Каждый элемент внутри из трех: путь к папке, папки внутри нашей, потом файлы. Следующий элемент - первая папка из предыдущего и то же самое для неё.
##for root, dirs, files in os.walk('.'):
##    ##print(root)
##    files = [f for f in files if len(f.split()[0]) > 7]
##whole_corp = ''
##for root, dirs, os.walk('.'):
##    for d in dirs:
##        if d.startswith('.'):
##            dirs.remove(d)
def rmtree(path):
    for root, dirs, files in os.walk(path, topdown=False):
        for f in files:
            os.remove(os.path.join(root, f))
        for d in dirs:
            os.rmdir(os.path.join(root,d))
        os.rmdir(path)
    print('Done!')

def drawtree(path):
    for root, dirs, files in os.walk(path):
        arr = []
        num = root.count('\\')
        new_root = root.split('\\')[-1]
        print('\t'*num+'--'+new_root+'\n')
        for f in files:
            print((num+1)*'\t'+f)

drawtree('.')

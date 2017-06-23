import os
import shutil
import re
def count_sentence():
    dictionary = {}
    for root, dirs, files in os.walk('news'):
        for f in files:
            with open(os.path.join(root, f), 'r', encoding='cp1251') as text:
                t = text.read()
            counter = len(re.findall('<se>', t))
            dictionary[f] = str(counter)
    return dictionary


def find_meta(text_str):
    author = re.search(r'<meta content="(.*)" name="author">', text_str).group(1)
    topic = re.search(r'<meta content="(.*)" name="topic">', text_str).group(1)
    arr = [author, topic]
    return arr

def write_to_csv(arr, name):
    with open(name, 'a', encoding='cp1251') as f:
        f.write(arr[2]+'\t'+arr[0]+'\t'+arr[1]+'\n')
                      
def write_s(smth, filename):
    with open(filename, 'a', encoding = 'utf-8') as f:
        f.write(smth)

def make_table():
    array_of_arr = []
    for root, dirs, files in os.walk('news'):
        for f in files:
            with open(os.path.join(root, f), 'r', encoding='cp1251') as text:
                t = text.read()
            arr = find_meta(t)
            arr.append(f)
            array_of_arr.append(arr)
    for arr in array_of_arr:
        write_to_csv(arr, 'table_meta.csv')
       
 def main():
    ##1 task
    d = count_sentence()
    for key in d.keys():
        write_s(key+'\t'+d[key]+'\n', 'sentences.txt')
    print('Done!')
    ##2 task
    make_table()
    print('Done!')
    ## 3 task
    


if __name__ == '__main__':
    main()


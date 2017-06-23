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
def get_text(text_str):
    text = re.sub('<.*?>', '', text_str)
    text = re.sub('\n', '', text)
    return text

def make_s(text_str):
    array_of_inf = []
    ds_arr = re.finditer(r'<se>(.*)?<\se>\n', text_str, flags=re.DOTALL)
    for d_sentence in ds_arr:
        d_sent = d_sentence.group(1)
        wordpos_arr = d_sent.split('\n')
        for i in range(len(wordpos_arr)):
            if re.search('gr="S,.*loc"', wordpos_arr[i]) != None:
                if i-1 > 0 and re.search('gr="PR"', wordpos_arr[i-1]) != None:
                    bigr = re.finditer(r'ana>(.*)</w>.*ana>(.*)</w>', wordpos_arr[i-1]+wordpos_arr[i])
                    bigr = bigr.group(1)+' '+bigr.group(2)
                    clear_sent = get_text(d_sent)
                    arr = [bigr, clear_sent]
                    array_of_inf.append(arr)
    return array_of_inf
    

def find_bigr():
    for root, dirs, files in os.walk('news'):
        for f in files:
            with open(os.path.join(root, f), 'r', encoding='cp1251') as text:
                t = text.read()
            array_of_inf = make_s(t)
            for i in array_of_inf:
                write_s(i[0]+'\t'+i[1], 'bigrams.txt')
        


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
    find_bigr()
    print('Done!')

if __name__ == '__main__':
    main()

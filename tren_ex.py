import re

def open_xml():
    ##читать по строкам
    with open('text.xml', 'r', encoding = 'utf-8') as f:
        text = f.readlines()
    return text


def open_xml_as_string():
    ##читать в одну строку
    with open('text.xml', 'r', encoding = 'utf-8') as f:
        text = f.read()
    return text


def write(string, filename):
    ##записать строку куда-нибудь
    with open(filename, 'w', encoding = 'utf-8') as f:
        f.write(string)


def count_ana_word(line_arr):
    ## считает число разборов на число словоформ
    n_arr = []
    for line in line_arr:
        if '<w' in line:
            num = len(re.findall('<ana ', line))
            n_arr.append(num)
    counter = sum(n_arr)/len(n_arr)
    return counter


def find_lex(text_str):
    ## Делает словарь типа "Часть речи: число вхожджений"
    lex_arr = [i.group(1) for i in re.finditer(r'gr=\"(.*?)(,|=)', text_str)]
    lex_d = {i: str(lex_arr.count(i)) for i in lex_arr}
    return lex_d
        

def get_text(text_str):
    ##убирает из текста все теги и переносы строк, возвращает массив слов с сохраненным регистром и знаками препинания
    text = re.sub('<.*?>', '', text_str)
    text = re.sub('\n', '', text)
    text_arr = text.split(' ')
    return text_arr


def find_ins(text_lines):
    ## находит в тексте слова которых есть разборы с творительным падежом и складывает их в массив
    words_ins = []
    for line in text_lines:
        if '=ins' in line:
            word = re.match('<w>(.*?)<', line).group(1)
            words_ins.append(word)
    return words_ins

def make_string(words_ins, text_arr):
    ## возвращает строку, как в задании
    line_arr = []
    text_arr_e = [i.strip('&.,?:"«»;!()') for i in text_arr] ##делает массив слов без знаков препинания
    for word in words_ins:
        n = text_arr_e.index(word) ##индекс слова в массиве
        left_context = [] ## делаю по отдельности левый и правый контекст
        for i in range(n-3, n-1):
            try:
                left_context.append(text_arr[i])
            except Exception: ## если вдруг нет в начале трех слов
                 continue
        right_context = []
        for i in range(n+1, n+3):
            try:
                right_context.append(text_arr[i])
            except Exception:
                break ##потому что если первого слова справа нет, то второго нет и подавно
        line = ' '.join(left_context)+'\t'+word+'\t'+' '.join(right_context)
        line_arr.append(line)
    string = '\n'.join(line_arr)
    return string

def main():
    ## Задание 1
    n = (count_ana_word(open_xml()))
    print(n)
    ## Задание 2
    gr_dict = find_lex(open_xml_as_string())
    array = [i+'\t'+gr_dict[i] for i in gr_dict.keys()]
    write('\n'.join(array), 'frq_gr.txt')
    ## Задание 3
    write((make_string(find_ins(open_xml()), get_text(open_xml_as_string()))), 'words_ins.txt')

if __name__ == '__main__':
    main()

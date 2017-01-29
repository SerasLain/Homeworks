import re
def openfile():
    with open(input(), 'r', encoding='utf-8') as f:
        text = f.read()
        text = text.split()
    return text
def normaltext(text):
    arr = []
    for i in range(len(text)):
        word = text[i].strip('.,?()"')
        arr.append(word.lower())
    return arr
def findword(regword, textarr):
    lex = []
    for i in range(len(textarr)):
        if re.search(regword, textarr[i]) != None:
            lex.append(textarr[i])
    return lex
def unique(a):
    uniquearr = []
    for i in range(len(a)):
        if a[i] not in uniquearr:
            uniquearr.append(a[i])
    return uniquearr
def main():
    regword = r'\bзагру(ж(у(сь)?|е(н(н(ая|о(е|й|го|му?)?|ы(х|е|й|ми?)|ую)?|[ыао]?|)))|з(ят(ся)?|и(те?(с[ья])?|шь(ся)?|л(ся|(а|о|и)(сь)?)?|м(ся)?|в(ш(и(х|ми?|й|е)?(с[ья])?|ую(ся)?|е(го|й|е|му?)(ся)?|ая?(ся)?)?)?)?))\b'
    text = normaltext('Введите путь к файлу: ', openfile())
    lex = unique(findword(regword, text))
    for i in lex:
        print(i)
main()

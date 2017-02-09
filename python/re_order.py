import re
def openarticle():
    with open(input('Введите путь к файлу: '), 'r', encoding='utf-8') as f:
        text = f.read()
    return text


def writeorderlist(order):
    with open(input('Введите путь к файлу: '), 'a', encoding='utf-8') as f:
        f.write(order)

        
def findorder(text):
    regwords = r'[W]Отряд:&nbsp;</td>\n<td width="60%" align="left"><a href=.*?>(Хищные)<'
    regword = r'Отряд.*?>([\w]*)</a></td>'
    matched = re.search(regword, text, flags = re.DOTALL)
    order = matched.group(1)
    return order


def main():
    writeorderlist(findorder(openarticle()))

main()

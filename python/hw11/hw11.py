import re
def openarticle():
    with open(input('Введите адрес файла со статьей: '), 'r', encoding = 'utf-8') as f:
        article = f.read()
    return article


def fintomal(article):
    newarticle = re.sub('Финлянди', 'Малайзи', article, flags = re.IGNORECASE)
    return newarticle


def writearticle(newarticle):
    with open(input('Введите адрес файла, в который записать новую статью: '), 'w', encoding = 'utf-8') as f:
              f.write(newarticle)

def main():
    writearticle(fintomal(openarticle()))


main()   
    

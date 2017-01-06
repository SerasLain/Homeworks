##6. Текст должен состоять из 5 предложений разных типов
##(утвердительные, вопросительные, отрицательные, условные, побудительные)
##на изучаемом вами языке (французский, испанский).
##Типы предложений должны выводиться в случайном порядке.
import random
def processing_n():
    ## возвращает список со словами из файла с существительными
    n = open('nouns.txt', 'r', encoding = 'utf-8')
    nouns = n.read()
    nouns = nouns.split()
    n.close()
    return nouns
def processing_v():
    ## возвращает список со словами из файла с глаголами в настоящем времени (3Sg)
    v = open ('verbs_PrInd.txt', 'r', encoding = 'utf-8')
    verbsPrInd = v.read()
    verbsPrInd = verbsPrInd.split()
    v.close()
    return verbsPrInd
def processing_q():
    ## возвращает список со словами из файла
    q = open ('questword.txt', 'r', encoding = 'utf-8')
    questwords = q.read()
    questwords = questwords.split()
    q.close()
    return questwords
def processing_vi():
    vi = open('verbs_Imp.txt', 'r', encoding='utf-8')
    verbimps = vi.read()
    verbimps = verbimps.split()
    vi.close()
    return verbimps
def processing_vpi1Sg():
    #возвращает глагол в простом настоящем времени первого лица единственного числа
    v1 = open('verbs_1SgPrInd.txt', 'r', encoding = 'utf-8')
    vp1 = v1.read()
    vp1 = vp1.split()
    v1.close()
    return vp1
def noun():
    ## возвращает существительное с артиклем
    nouns = processing_n()
    k = random.choice(nouns)
    ## исправляем косяк в файле с отсутствем артиклей ad hoc
    if nouns.index(k) > 81:
        return ('el '+ k)
    return ('la '+ k)
def verb():
    ## возвращает глагол в настоящем времени
    verbsPrInd = processing_v()
    verbpi = random.choice(verbsPrInd)
    return verbpi
def verb_imp():
    ##возвращает глагол в форме императива
    verbimps = processing_vi()
    verbi = random.choice(verbimps)
    return verbi
def questword():
    qws = processing_q()
    qw = random.choice(qws)
    return qw
def verbPr1Sg():
    vp1 = processing_vpi1Sg()
    v = random.choice(vp1)
    return v
def sentencer(s, t="."):
    ## делает из массива a нормальное предложение
    st = ' '.join(s)
    st += t
    st = st.capitalize()
    return st
def declar():
    ## для повествовательных
    decl = [noun(), verb(), noun()]
    return sentencer(decl)
def negat():
    ## для отрицательных
    negat = [noun(), 'no', verb(), noun()]
    return sentencer(negat)
def interrog():
    ## для вопросительных
    interrog = [questword(), noun(), verb(), noun()]
    return '¿' + (sentencer(interrog, t="?"))
def imper():
    ## для побудительных
    imper = [verb_imp(), noun()+',', ' por favor']
    return sentencer(imper)
def condit():
    ## для условных
    d = random.random()
    if d == 0:
        verb1 = verb()
    else:
        verb1 = verbPr1Sg()
    t = random.random()
    if t == 0:
        verb2 = verb()
    else:
        verb2 = verbPr1Sg()
    condit = ['si', verb1+',', verb2]
    return sentencer(condit)
def main():
    sentencesbox = [declar(), negat(), interrog(), imper(), condit()]
    random.shuffle(sentencesbox)
    for i in range(len(sentencesbox)):
        print(sentencesbox[i])
main()

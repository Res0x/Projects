chars = '[]!#$%&"*+-=?,@^_(). '
eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
def is_valid(num):
    if num.isdigit():
        return True
    else:
        return False

def language_trust(st, lang):
        if lang == 'en' and rus_upper_alphabet not in st and rus_lower_alphabet not in st:
            return True
        elif lang == 'ru' and st not in eng_upper_alphabet and st not in eng_lower_alphabet:
            return True
        return False
def language_checker(ln):
    if ln == 'en' or ln == 'ru':
        return True
    return False

def coding(text, language, n):
    res = []
    if language == 'en':
        for i in text:
            if i.isdigit() or i in chars:
                res.append(i)
                continue
            if i.isupper():
                res.append(chr(ord("A") + (ord(i) - ord("A") + 26 + int(n)) % 26))
            else:
                res.append(chr(ord("a") + (ord(i) - ord("a") + 26 + int(n)) % 26))

    elif language == 'ru':
        for i in text:
            if i.isdigit() or i in chars:
                res.append(i)
                continue
            if i.isupper():
                res.append(chr(ord('А') + (ord(i) - ord('А') + 32 + int(n)) % 32))
            else:
                res.append(chr(ord('а') + (ord(i) - ord('а') + 32 + int(n)) % 32))
    return(res)

def start():
    print('Выбери язык (ru или en)')
    l = input()
    while not language_checker(l):
        print('Вы ввели неверное значение')
        l = input()
    print('Напиши текст который ты хочешь закодировать')
    t = input()
    while not language_trust(t, l):
        print('Вы ввели сообщение не на том языке который выбрали')
        t = input()
    print('Выбери сдвиг')
    m = input()
    while not is_valid(m):
        print('Вы ввели неверное значение')
        m = input()
    print(*coding(t, l, m), sep='')

start()
import random

def char_is_num(n):
    while True:
        try:
            if int(n) <= 0:
                n=input("Число должно быть положительным! Попробуйте ещё раз: ")
            else:
                return int(n)
        except ValueError:
            n=input("Введите целое положительное число: ")

def yes_or_no(f):
    while True:
        if f=='Да':
            return True
        elif f=='Нет':
            return False
        else:
            f=input("Введите Да/Нет! Попробуйте ещё раз: ")

def generate_password(length,chars):
    s=''
    for i in range(length):
        s+=random.choice(chars)
    return s

digits='0123456789'
lowercase_let='abcdefghijklmnopqrstuvwxyz'
uppercase_let='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation= '!#$%&*+-=?@^_.'

chars = ''
k=char_is_num(input("Введите кол-во паролей для генерации: "))
length=char_is_num(input("Введите длину пароля: "))

dig_f=yes_or_no(input("Включать ли цифры? Введите Да/Нет: "))
lowlet_f=yes_or_no(input("Включать ли прописные буквы? Введите Да/Нет: "))
upplet_f=yes_or_no(input("Включать ли строчные буквы? Введите Да/Нет: "))
punf=yes_or_no(input("Включать ли символы? Введите Да/Нет: "))
digf=yes_or_no(input("Исключать ли неоднозначные символы il1Lo0O? Введите Да/Нет: "))

if dig_f:
    chars+=digits
if lowlet_f:
    chars+=lowercase_let
if upplet_f:
    chars += uppercase_let
if punf:
    chars += punctuation
if upplet_f:
    symremove = "il1Lo0O"
    for i in symremove:
        chars = chars.replace(i, "")

print("\nСгенерированные пароли:")
for i in range(k):
    print(generate_password(length, chars))

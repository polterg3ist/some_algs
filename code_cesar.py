alph = 'abcdefghijklmnopqrstuvwxyz'
code = {alph[i]: alph[i+3] for i in range(0, len(alph) -3)}
uncode = {alph[i+3]: alph[i] for i in range(0, len(alph) -3)}
lasts = {'x': 'a', 'y': 'b', 'z': 'c', ' ': ' '}
uncd_last = {'a': 'x', 'b': 'y', 'c': 'z', ' ': ' '}

ru_alph = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
ru_code = {ru_alph[i]: ru_alph[i+3] for i in range(0, len(ru_alph) -3)}
ru_uncode = {ru_alph[i+3]: ru_alph[i] for i in range(0, len(ru_alph) -3)}
ru_lasts = {'э': 'а', 'ю': 'б', 'я': 'в', ' ': ' '}
ru_uncd_last = {'a': 'э', 'б': 'ю', 'в': 'я', ' ': ' '}

code.update(lasts)
uncode.update(uncd_last)
ru_code.update(ru_lasts)
ru_uncode.update(ru_uncd_last)

choose_lang = input('Two language are aviable: enter 1/2 for ru/eng: ')

if choose_lang == '1':
    lang_code = ru_code
    lang_uncode = ru_uncode
elif choose_lang == '2':
    lang_code = code
    lang_uncode = uncode
else:
    print('Incorrect input! As default was choosen english.')
    lang_code = code
    lang_uncode = uncode
    
    
while True:
    choose_oper = input('Write 1 to encode, 2 to decode, 3 to exit: ')
    if choose_oper == '3':
        break
    
    elif choose_oper == '1':
        coded = ''
        text = input('Write text: ').lower()
        for i in text:
            if i in lang_code:
                coded += lang_code[i]
            else:
                coded += i
                
    elif choose_oper == '2':
        coded = ''
        text = input('Write text: ').lower()
        for k in text:
            if k in lang_uncode:
                coded += lang_uncode[k]
            else:
                coded += k
    else:
        print('Wrong operation!')
        continue
    print(coded)
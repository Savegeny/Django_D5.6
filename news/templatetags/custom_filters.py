from django import template

register = template.Library()

spisok_mat = [
    'мат1',
    'мат2',
    'мат3',
    'Мат1',
    'Мат2',
    'Мат3',
    'МАТ1',
    'МАТ2',
    'МАТ3',
    'мат_1',
    'мат_2',
    'мат_3',
    'Мат_1',
    'Мат_2',
    'Мат_3',
    'мат_4',
    'allposttext',
    'хрень',
]

symbol = [
    ',',
    '.',
    '!',
    '@',
    '#',
    '$',
    '%',
    ':',
    '&',
    '?',
    '*',
    '(',
    ')',
    '-',
    '_',
    '+',
    '=',
    '''"''',
    '''''''',
]

@register.filter(name='Censor')
def Censor(value, arg):
    if isinstance(value, str) and isinstance(arg, int):
        for w in value.split():
            w_rep = w.lower()
            if w_rep in spisok_mat:
                value = value.replace(w_rep, '*' * arg)
            else:
                for s in symbol:
                    w_rep = w_rep.replace(s, '')
                    if w_rep in spisok_mat:
                        value = value.replace(w_rep, '*' * arg)
        return value
    else:
        raise ValueError(f'Нельзя умножить ''*'' на {type(arg)}')
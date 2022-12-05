def a():
    print('a')

def b():
    print('b')

def c():
    print('c')

def_list = {
    'a': a,
    'b': b,
    'c': c
}

def_active = [
    'a', 'b'
]

for active in def_active:
    if active in def_list.keys():
        def_list[active]()
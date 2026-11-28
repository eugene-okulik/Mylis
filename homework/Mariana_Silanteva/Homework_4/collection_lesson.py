my_dict = {
    'tuple': (1, 'text', True, 3.6, 9),
    'list': [1, 5, 'example', False, 9.3],
    'dict': {
        'country': 'USA',
        'capital': 'Washington',
        'language': 'english',
        'currency': 'USD',
        'has_mountains': True
    },
    'set': {3, 6, 'news', True, 2.7}
}

print(my_dict['tuple'][-1])

my_dict['list'].append('new_text')
my_dict['list'].pop(1)

my_dict['dict'][('i am a tuple',)] = False
del my_dict['dict']['currency']

my_dict['set'].add('text')
my_dict['set'].remove(6)

print(my_dict)

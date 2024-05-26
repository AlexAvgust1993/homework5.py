immutable_var = 1, 2, 3, 4, 'fire'
print('Immutable: ' ,immutable_var)
immutable_var_1 = (1, 2, 3, 4, 'fire')
print('Immutable: ', immutable_var_1)
immutable_var_2 = tuple([1, 2, 3, 4, 'fire']) # мы видим что кортеж изменению не подлежит
print('Immutable: ', immutable_var_2)
#print('Changed: ', immutable_var[1] = 5)

mutable_list = ['fire', 'water', 'earth']
print('Mutable list: ',mutable_list)
mutable_list[2] = 'metal'
print('Changed: ',mutable_list)
mutable_list.append('air')
print('Changed: ',mutable_list)


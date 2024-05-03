# sets = {12, 'sf', 12,  2.1} # 15:9
# set2 = {12, 'sf', 34, 'sds'}
# print(len(sets))
# sets.add(132)
# print(sets)

# sets.update([3,4,5])
# print(sets)

# intersection = sets.intersection(set2)
# print(intersection)


# set2.remove(12)
# print(set2)

# result = set2.difference(sets)
# print(result)

# sets.intersection_update(set2)
# print(sets)


# sets.clear()
# print(sets)


# sets.discard(11)
# print(sets)

# popped = sets.pop()
# print(popped)
# print(sets, f"из множества удалили {popped}")

# glasnye = {'a', 'i', 'o', 'e', 'u', 'y'}
# letter = input('any letter: ')
# limit = 1
# if letter.lower()in glasnye :
#     print(True)
# elif len(letter) > limit:
#     print('no more than 1 letter')
# else:
#     print(False)


set1 = {1,2,3,4,5}
set2 = {1,3,5,7,9}

# set2.remove(7)
# print(set2)


# inter = set1.intersection(set2)
# print(inter)


# differ= set1.difference(set2)
# print(differ)

# set1.add('hello')
# popped = set1.pop()
# print(set1, f"popped item {popped}")



dict1 = {
    #key : value
    'Kyrgyzstan' : 'Bishkek',
    'kazakhstan' : 'Astana',
    'Uzbekstan' : 'Tashkent'
}

# print(dict1['Kyrgyzstan'])
# dict1["USA"] = 'Vashington' # добавление в словарь
# print(dict1)


# dict1.clear()
# print(dict1)


# value = dict1.get('kazakhstan')
# print(value)


# keys = dict1.keys()
# print(keys)

# values = dict1.values()
# print(values)

# items = dict1.items()
# print(items)

# dict1.update({12 : 'twelve', 'name' : 'oomat'})
# print(dict1)


# tuple = list((1,2,3,4))
# print(type(tuple))

list = dict([('name', 2), ('dsf', 23)])
print(type(list))
print(list)
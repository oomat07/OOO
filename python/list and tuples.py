my_tuple = tuple((12, 12.4, True, False, 'ok', (1, 34)))

# print(my_tuple) # выводит кортеж
# print(my_tuple[2]) # обравщается по индексу
# print(my_tuple[2:5:2]) # срез с отступом 2
# print(len(my_tuple)) # счтает элементы


new_tuple = my_tuple + (15, 'oma',)
print(str(new_tuple))
list2 = (1222, 'dsfasf')

l1st = [232.3, True, '12', 12, 12, 12] 
l1st.append(list2)
print(l1st)
print(l1st.index(12))

list2 = [11, 344, 32]
l1st.extend(list2)
print(l1st)

count = l1st.count(12)
print(count)

l1st.remove(12)
print(l1st)

# poped = l1st.pop(6)
# print(poped)
# print(l1st)


list1 = ['oomat ', 'belek ', 'aziz ', 'beka ', 'aiperi ']

string = ''
joined = string.join(list1)

print(joined)


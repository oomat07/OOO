# def hello():
#     print('playboy')

# hello()


# def add(a, b):
#     return a + b

# result = add('b', 'q')
# print(result)

# names = ['oomat']
# passwords = [1234]

# try:
#     name = input("Введите имя: ")
#     password = int(input('Введите пароль: '))
# except NameError and ValueError:
#     print("cant found password")

# def acces(name=name, password=password):
#     if name in names and password in passwords:
#         print('acces is open')
#     elif name not in names and password not in passwords:
#         print('both of them are incorrect')
#     elif name not in names:
#         print("name is incorrect")
#         print("name is incorrect")
#     elif password not in passwords:
#         print('password incorrect')
#     else:
#         print("acces is close")

    # if name in names:
    #     if password in passwords:
    #         print('open access')
    #     else:
    #         print('password incorrect')
    # else:
    #     print('name is incorrect')



# acces()


# def reversed_half(list1):
#     half = len(list1) // 2
#     list1[:half] = reversed(list1[:half])
#     list1[half:] = reversed(list1[half:])
#     return list1
# lst = ['oomat', 'name', 16, 12]
# res = reversed_half(lst)
# print(res)



# a = min(12,222,34,2)
# b = max(12, min(3, 50), abs(-13), max(12, 34, 4))
# print(b)

# def square(a):
#     return a ** 2

# so = square(222)
# print(so)

# x = int(input('number: '))
# def even(x): 
#     return x + 1

# print(even(x))

# def bolshe(num):
#     if num <= 100:
#         return f'your number {num}'
#     else:
#         return 'incorrect num '
# print(bolshe(even(x)))


# a,*b,c = [1,3,45,5,6,76,7,2,3]
# print(a,b,c)

# def func(a, b,c,d):
#     return a, b, c, d

# print(func(1,2,3,4))
# a = ['hello', True, 234, [1,2,4]]

# print(func(*a))


# def func1(*nums):
#     res = 0
#     for num in nums:
#         res += num
#     return res
# print(func1(1,2,4,5,6,76,78,8))


# def func(**kwargs):
#     for num, val in kwargs.items():
#         print(num, val)
# func(a=12, b=122, name='sfes')

# def student(name, **lessons):
#     print(f"hello, {name}")
#     for names, times in lessons.items():
#         print(f"{names} : {times}")
# student('Oomat', chemstry =4, math=7, kyrgyzlang= 5)


# вложеные функции

# def main(name):
#     print('hello')
#     def inner():
#         print('hello', name)
#     inner()

# main('oomat')



# def my_func(integer):
#     def inner(num):
#         return integer + num
#     res = inner(100)
#     print(res)
# my_func(100)


# def total_callory():
#     p = products
#     def count_callory(p):
#         res = 0
#         for i in p.values():
#             res+=i
#         return res
#     print(count_callory(p))

# products = {
#     'aplle':108,
#     'bread':200,
#     'egg':300
# }

# total_callory()


# closure  замыкание


# def sum(a):
#     def inner(b):
#         return a + b
#     return inner

# inner = sum(1)
# print(inner(10))
# print(inner(500))
# print(inner(110))

# def sum():
#     a = 100
#     def inner(b):
#         return a + b
#     return inner
# s = sum()
# print(s(50))



# decorators


# def decorator(func):
#     def inner():
#         print('hello')
#         func()
#         print('finish')
#     return inner

# @decorator
# def func():
#     print("oomat")

# func()



import random 

def unical(random_100):
    def individual():
        result = list(random_100())
        res = random.choices(result, k=50)
        res = list(set(res))
        random.shuffle(res)
        print(res)
    return individual

@unical
def random_100():
    lst = []
    for i in range(100):
        result = random.randint(10, 50)
        lst.append(result)
    return lst

random_100()
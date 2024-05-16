# def func(x):
#     if x < 4:
#         print(x)
#         func(x+1)
#         print(x)
# func(1)


# def summa(x):
#     num = 0
#     for i in range(1, x+1):
#         num += i
#     return num
# print(summa(5))

# def summa(x):
#     if x == 1:
#         return 1
#     else:
#         return x + summa(x-1)
# print(summa(10))


# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n-1)
# print(fact(3))


# def sum(a, c):
#     return a + c

# print(sum(12, 2))


# l = lambda b, o: b + o
# print(l(11, 22))

# p = lambda num: True if num > 5 else False
# print(p(3))


# def compare(n):
#     if n>5:
#         return True
#     else:
#         return False
# print(compare(12))


# lst = [12,234, lambda : 'oomat' ,45,5]
# print(lst[2]())

# l1st = [12,3,4,5,6,67]

# def get_filter(a, filter=None):
#     if filter is None:
#         return a
#     else:
#         result = []
#         for i in a:
#             if filter(i):
#                 result.append(i)
    
#     return result

# print(get_filter(l1st, lambda x: x > 5))


# def sets(sss):
#     if not sss:
#         return sss
#     delete = sss.pop()
#     print(delete)
#     s = sets(sss)
#     return s  

# sett = {12,32,4,5,6,6,7,}
# print(sets(sett))
# import time
# # from functools import wraps
# #
# #
# #
# #
# # def g_outer(x):
# #     def outer(func):
# #         @wraps(func)
# #         def wrapper(*args, **kwargs):
# #             result = func(*args, **kwargs)
# #             return result
# #
# #         return wrapper
# #     return outer
# #
# # @g_outer(33)
# # def func(name, age):
# #     print(f'my name id:{name}......my age is:{age}')
# #     return name
# #
# # func('mzy', 18)
# # print(func)
# #
# # def func1():
# #     print('a')
# #
# # def func2():
# #     print('b')
# #
# # def repir(x, y):
# #     res = func1() if x > y else func2()
# #
# # repir(1,2)
# #
# #
# # l = ['abc', 'asf', 'fsdgabc']
# #
# # new_l = [news for news in l if news.endswith('abc')]
# # print(new_l)
# #
# #
# # def sum1(i):
# #     if i == 0:
# #        return i
# #     return i + sum1(i - 1)
# #
# # print(sum1(10))
#
# l = [1, 2, [3, 4, [5, 6, [7, 8]]]]
#
# def func(li):
#     for i in li:
#         if type(i) is list:
#             return func(i)
#         else:
#             print (i)
#
# # func (l)
# #
# #
#
#
#
#
#
#
#
#
#
#
#
#
# l = [1, 2, [3, 4]]
#
# def func(li):
#     for i in li:
#         if type(i) == list:
#             func(i)
#         else:
#             print(i)
#
# func(l)
#
# l = ['a','b','c','d']
#
# def per(l,level):
#     if level == len(l):
#         print(l)
#     for i in range(level, len(l)):
#         l[i], l[level] = l[level], l[i]
#         per(l, level+1)
#         l[i], l[level] = l[level], l[i]
#
# per(l,0)

# l = [1, 2, [3, 4]]

# def func(l):
#     for i in l:
#         if type(i) == list:
#             func(i)
#         else :
#             print(i)
#
# func(l)
#
# s = 'ab'
# l = list(s)
# def func(l, level):
#     if level == len(l):
#         print(l)
#     for i in range(level, len(l)):
#         l[i], l[level] = l[level], l[i]
#         func(l, level+1)
#         l[i], l[level] = l[level], l[i]
#
# func(l, 0)
#
# l = [1,2,3,4]
#
# def func(li, num):
#     if len(li) == 0:
#         print('没找到')
#     if num > li[int(len(li)/2)]:
#         li = li[int(len(li)/2)+1:]
#         func(li, num)
#     elif num < li[int(len(li)/2)]:
#         li = li[:int(len(li)/2)]
#         func(li, num)
#     elif num == li[int(len(li)/2)]:
#         print(li[int(len(li)/2)])
#     else:
#         pass
#
#
# func(l, 4)
#
# info = {
#     'a':1,
#     'b':3,
#     'c':2
# }
#
# res = max(info, key=lambda x:info[x])
# print(res)
#
#
#
# l = ['a','b','c','d']
#
# res = map(lambda name:name+'w',l)
# print(res.__next__())
# print(res.__next__())
#
# alter table mytable motify name int
# # alter table mytable change My
# # alter table mytable rename yourtable
# print('错误！')
# # print('对')
# # msg = 'sdsadasdasdasd'
# # def my(msg):
# #     print(f'{msg}')
# #
# # my(msg)
# # import sys
# # sys.path.append('E:\my2')
#
# import os
# import time
# # base_dir = os.path.dirname(os.path.dirname(__file__))
# # print(base_dir)
# # logpath = rf'{base_dir}\pythonProject1\log'
# print(time.time())
# print(time.strftime('%Y-%m-%d %X', time.localtime()))
# print(time.localtime())
# print(time.localtime(time.time()))
# import datetime
#
# print(datetime.datetime.now().replace(microsecond=0)+datetime.timedelta(days=1))
#
# print(time.strftime('%Y-%m-%d %X', time.localtime(11111111)))
# t = '1983-12-12 12:12:12'
# res = time.strptime(t, '%Y-%m-%d %H:%M:%S')
# print(res)
# print(time.mktime(res))
import os
import time
# # print(os.getcwd())
# # os.chdir('..')
# # os.makedirs('mkdir1/mkdir2')
# # os.remove(r'..\mkdir1\mkdir2\aaa.py')
# # os.rmdir(r'..\mkdir1\mkdir2')
# print(os.environ['COMMONPROGRAMFILES'])
# print(os.getenv('COMMONPROGRAMFILES'))
# print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.stat(r'..\pythonProject1').st_atime)))
# print(os.name)
# print(os.path.split(os.getcwd()))
# print(os.path.dirname(os.getcwd()))
# print(os.path.basename(r'E:\my2\pythonProject\.idea\modules.xml'))
import sys

print(sys.argv)

import shutil
def outer(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result

    return wrapper

def g_outer(x):
    def outer(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result

        return wrapper
    return outer
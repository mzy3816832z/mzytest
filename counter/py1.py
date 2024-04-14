# import os
#
# def count_files(path, size):
#     for i in os.listdir(path):
#         now_path = os.path.join(path, i)
#         if os.path.isfile(now_path):
#             size += os.path.getsize(now_path)
#         else:
#             size += count_files(now_path, size)
#     return size
#
#
# print(count_files(r'E:\my2\counter', 0))
#
import shutil
# import json
#
# # shutil.make_archive(r'E:\my2\counter2', 'zip',  root_dir=r'E:\my2\counter\py1.py')
# dic = {'name': 'mzy', 'age': 18, 'salary': 3.5, 'married': False, 'hobby': ['可乐', '游戏']}
# print(json.dumps(dic))
#
# import configparser
# config = configparser.ConfigParser()
# config.read('aaa.ini', encoding='utf-8')
# print(config.sections())
# print(config.options('mzy'))
# print(config.items('mzy'))
# a = config.getboolean('mzy', 'c')
# # print(a, type(a))
# import subprocess
#
# obj = subprocess.Popen('dir & asdasd', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#
# res = obj.stdout.read()
# print(res.decode('GBK'))
#
# res_error = obj.stderr.read()
# print(res_error.decode('GBK'))

import hashlib

# h1 = hashlib.md5('abc'.encode('utf8'))
# h1.update('123'.encode('utf-8'))
# print(h1.hexdigest())
#
#
#
#
# h2 = hashlib.sha256('abc'.encode('utf-8')).hexdigest()
# print(h2)
# import os
# h4 = hashlib.md5()
# size = os.path.getsize(r'E:\my2\abc')
# out_size = size//3
# with open(r'E:\my2\abc', 'rb') as f:
#     print(f.read())
#     for i in range(3):
#         f.seek(i*out_size, 0)
#         print(f.read(3))
#         h4.update(f.read(3))
#     print(h4.hexdigest())
#
# h5 = hashlib.md5('012789cde'.encode('utf-8'))
# abb = h5.hexdigest()
# print(abb)
# print('012789cde'.encode('utf-8'))
#
# a = 'asdasd1q231'
# b ='''xyz
# asdasd1q231
# asdasd1q231
# xsdasd1q231'''
#
# c='''13063527322    18509914998
# 134648814516161
# 64564561564
# asdasdasdas
# 13809956010
# 1306asxsaxa
# 13063527322'''
import re
#
# print(re.findall('.+', '123\nfasf', flags=re.S))
# print(re.findall('^x', b, flags=re.M))
# print(re.findall(r'\b(?:13[0-9]|18[0-9])\d{8}\b', c, flags=re.M))
# print(re.search(r'\b(?:13[0-9]|18[0-9])\d{8}\b', c).group())
#
# _json = ('''a: a
#          b: b''')
# print(re.sub(r'\d', '*', c))
# res = re.finditer(r'(\w*):(.*)', _json)
# z = {}
# for i in res:
#     z[i.group(1)] = i.group(2)
# print(z)
#
# s = 'xyg,- time,    !dog,    cat'
# print(re.split(r'\W+', s))
#
import logging
logging.basicConfig(
    level=10,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y',filename=r'E:\my2\counter\aaa.ini')

logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')

c = 1
s = 2
f = 5
t = 5
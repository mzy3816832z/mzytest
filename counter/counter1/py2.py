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

shutil.copyfile(r'E:\my2\counter\py1.py', r'E:\my2\counter\counter1\py2.py')
shutil.move(r'E:\my2\counter\counter1', r'E:\my2\pythonProject')
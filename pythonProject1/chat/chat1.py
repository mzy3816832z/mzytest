from pythonProject import outer

def chat(logpath):
    with open(logpath, mode='wt',encoding='utf-8' )as f:
        f.write('记录1')

chat(logpath=outer.logpath)
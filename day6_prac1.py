with open ('todo.txt','w',encoding='utf-8') as f:
    f.write('吃饭\n')
    f.write('喝水\n')
    f.write('睡觉\n')
print('写入完成')

with open ('todo.txt','r',encoding='utf-8') as f:
    content = f.read()
print('读到的内容：')
print(content)
#第一题
fruits = ['苹果','香蕉','橙子','葡萄']
print(fruits[0])
print(fruits[-1])
#第二题
fruits[1] = '西瓜'
print(fruits)
#第三题
fruits.append('芒果')
print(len(fruits))
#第四题
for x in fruits:
    print(x)
#第五题
print(fruits[0:2])
#第六题
t = (100,200,300)
print(t[1])
#t[0]=99
#TypeError: 'tuple' object does not support item assignment
#因为当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来
#第七题
total = 0
nums = [5,10,15,20]
for x in nums:
    total = total + x
print(total)
#第八题
student = {'name':'素林','age':30,'weight':165}
print(student['name'])
print(student['weight'])
student['target']= 150
print(student)
#第九题
for s in student:
    print(f'{s} : {student[s]}')
#第十题
aaa = [{'name':'qwe','score':'88'},{'name':'asd','score':'89'},{'name':'zxc','score':'68'}]
for fu in aaa:
    print(f'{fu['name']}:{fu['score']}')
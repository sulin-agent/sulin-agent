#第一题
n=17
if n % 2 ==1:
    print('奇数')
else:
    print('偶数')
#第二题
score=85
if score >= 90:
    print('优秀')
elif score >= 75:
    print('良好')
elif score >= 60:
    print('及格')
else:
    print('不及格')
#第三题
num = 12
if num > 0:
    if num % 2 == 0:
        print('正偶数')
    else:
        print ('正奇数')
else:
    print('非正数')
#第四题
total = 0
for a in range(1,101):
    total=total+ a
print(total)
#第五题
nums = [10,25,48,53,60,7]
for n in nums:
    if n > 50:
        print(n)
        break
#第六题
range(1,11)
for a in range(1,11):
    if a % 3 == 0:
        continue
    print(a)
#第七题
count = 10
while count > 0:
    print(count)
    count = count - 1
print('发射')
#第八题
passwords = ['0000','1234','9999']
correct = '1234'
for p in passwords:
    if p == correct:
        print('密码正确，登陆成功')
        break
    else:
        print(f'尝试 {p} 错误')
#第九题
nums = [1,2,3,4,5,6]
for n in nums:
    if n % 2 == 0:
        print(n)
#第十题
d = [{'name':'东方红','weight':78,'height':1.75},{'name':'儿童','weight':73,'height':1.77},{'name':'认识','weight':90,'height':1.72}]
normal_count=0
for x in d:
    bmi = x['weight']/x['height']**2
    print(f"{x['name']} bmi: {bmi:.2f}") 
    if bmi <18.5:
        print('偏瘦')
    elif bmi <24:
        print('正常')
        normal_count = normal_count +1
    elif bmi < 28:
        print('过重')
    else:
        print('肥胖')
print(f'正常人数：{normal_count}')
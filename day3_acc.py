# 累加器练习（参考版，建议你自己重敲一遍）
# 任务：算 1+2+3+...+10 的和，结果应该是 55

uuu = 0
for y in range(101):
    uuu = uuu + y
print(uuu)

L=['bart','lisa','adam']
for p in L:
    print('hello,' ,p,'!!!')

hhh=0
f=100
while f >= 0:
    hhh=hhh+f
    f=f-2
print(hhh)

n=0
while n < 100:
    n=n+1
    if n % 2 ==0:
        continue
    print(n)
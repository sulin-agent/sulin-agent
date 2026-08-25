# intro.py —— Day 2 必做练习：变量与数据类型
# 运行方式：在 VS Code 里打开本文件，点右上角的 ▶ 运行；
#           或者在终端里 cd 到这个文件夹，输入  python intro.py

# 1) 变量 = 装数据的盒子。给盒子起名字，往里放数据。
name = "素林"        # 字符串 str：用引号包起来的文字
age = 30             # 整数 int：没有小数点的数字（按你实际情况改）
weight = 165         # 整数 int：当前体重（斤）
target = 150         # 整数 int：目标体重（斤）
height = 1.75        # 小数 float：身高（米）
is_studying = True   # 布尔 bool：不是真(True)就是假(False)

# 2) type() 看看每个盒子里装的是什么类型
print(type(name))           # <class 'str'>
print(type(weight))         # <class 'int'>
print(type(height))         # <class 'float'>
print(type(is_studying))    # <class 'bool'>

# 3) 字符串拼接：用 + 把文字连起来
greeting = "你好，" + name
print(greeting)

# 4) f-string：在字符串前面加 f，用 {变量} 把数据嵌进去（今天主角）
print(f"我叫{name}，今年{age}岁")
print(f"我当前体重{weight}斤，目标{target}斤")

# 5) 算一下还要减多少斤，并打印自我介绍
need_lose = weight - target
print(f"大家好，我是{name}，目前{weight}斤，距离目标还差{need_lose}斤，加油！")

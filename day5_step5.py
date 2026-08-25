from tools import bmi, bmi_level
people = [
    {'name': '张三', 'weight': 80, 'height': 1.75},
    {'name': '李四', 'weight': 55, 'height': 1.62},
    {'name': '王五', 'weight': 90, 'height': 1.70},
]
for p in people:
    b=bmi(p['weight'],p['height'])
    print(f'{p['name']}的bmi是:{b:.2f},分级是：{bmi_level(b)}')
def bmi(weight,height):
    return weight / (height*height)
def bmi_level(bmi):
    if bmi < 18.5:
        return '偏瘦'
    elif bmi < 24:
        return "正常"
    elif bmi < 28:
            return "偏胖"
    else:
        return "肥胖"
print(bmi_level(22))
print(bmi_level(17))
print(bmi_level(30))
print(bmi_level(bmi(80, 1.75)))
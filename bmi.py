# bmi.py —— Day 2 练手：BMI 小计算
# BMI = 体重(公斤) / 身高(米)的平方
# 注意：前面 weight 记的是"斤"，这里要先换算成公斤（斤 ÷ 2）

name = "素林"
weight_jin = 165        # 当前体重（斤）
height = 1.75           # 身高（米）
weight_kg = weight_jin / 2   # 斤转公斤

bmi = weight_kg / (height * height)
print(f"{name} 的 BMI 是：{bmi:.1f}")   # :.1f 表示只保留 1 位小数

# —— 下面这段 if 判断是 Day 4 才正式学的，先放这儿看个眼熟，看不懂先跳过 ——
if bmi < 18.5:
    status = "偏瘦"
elif bmi < 24:
    status = "正常"
else:
    status = "偏重"
print(f"体型判断（先了解）：{status}")

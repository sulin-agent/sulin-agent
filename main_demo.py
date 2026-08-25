# main_demo.py —— 这是主程序，它 import 了 module_a

print("【main_demo】主程序开始")
import module_a   # 这一行会触发 module_a 里的"顶层代码"

print("【main_demo】调用 module_a 的函数：", module_a.greet("世界"))

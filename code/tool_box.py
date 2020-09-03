import tools
print("                                                           Bona陈独家制作，严禁转载！")
print("欢迎使用Bona的工具箱")
fault_start = 0
while True:
    if fault_start != 1:
        print("您想要使用什么工具呢？")
    admit_start = input("""A.掷硬币模拟器  B.闰年计算器  C.退出
：""")
    if admit_start == "A":
        fault_start = 0
        from tools import coins
    elif admit_start == "B":
        fault_start = 0
        from tools import leap_year
    elif admit_start == "C":
        fault_start = 0
        print("谢谢使用")
        break
    else:
        fault_start = 1
        print("请输入大写的A/B/C")

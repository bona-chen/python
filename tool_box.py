print("                                                           Bona陈独家制作，严禁转载！")
print("欢迎使用Bona的工具箱")
fault_start = 0
while True:
    if fault_start != 1:
        print("您想要使用什么工具呢？")
    admit_start = input("""A.掷硬币模拟器  B.闰年计算器  C.退出
：""")
    if admit_start == "A":
        import random

        admit = input("请问您想掷多少次硬币？\n:")
        while admit.isdigit() == 0:
            admit = input("请输入阿拉伯数字:")
        times_admit = int(admit)
        print("实验开始了!:")
        times = 0
        front = 0
        back = 0
        continuous_front_here = 0
        continuous_front_there = 0
        continuous_back_here = 0
        continuous_back_there = 0
        while times < times_admit:
            answer = random.randint(1, 2)
            if answer == 1:
                print("正面", end=(" "))
                front += 1
                continuous_front_there += 1
                if continuous_back_there > 0:
                    continuous_back_there = 0
                if continuous_front_there > continuous_front_here:
                    continuous_front_here = continuous_front_there
                times += 1
            else:
                print("反面", end=(" "))
                back += 1
                continuous_back_there += 1
                if continuous_front_there > 0:
                    continuous_front_there = 0
                if continuous_back_there > continuous_back_here:
                    continuous_back_here = continuous_back_there
                times += 1
        else:
            print("\n一共掷了 ", times_admit, " 次硬币。结果:")
            print("正面一共", front, " 次")
            print("反面一共:", back, " 次")
            print("最多连续正面", continuous_front_here, "次")
            print("最多连续反面", continuous_back_here, "次")
    elif admit_start == "B":
        admit = input("请输入年份:")
        if admit.isdigit() == 0:
            admit = input("请输入阿拉伯数字:")
        year = int(admit)
        if year % 400 == 0:
            print("该年份是闰年")
        elif year % 100 == 0:
            print("该年份不是闰年")
        elif year % 4 == 0:
            print("该年份是闰年")
        else:
            print("该年份不是闰年")
    elif admit_start == "C":
        print("谢谢使用")
        break
    else:
        fault_start = 1
        print("请输入大写的A/B/C")

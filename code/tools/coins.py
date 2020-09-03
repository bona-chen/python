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
        print("正面", end=" ")
        front += 1
        continuous_front_there += 1
        if continuous_back_there > 0:
            continuous_back_there = 0
        if continuous_front_there > continuous_front_here:
            continuous_front_here = continuous_front_there
        times += 1
    else:
        print("反面", end=" ")
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

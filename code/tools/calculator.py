choose = input("A.加法  B.减法  C.乘法  D.除法\n: ")
while choose != "A" and choose != "B" and choose != "C" and choose != "D":
    print("请输入大写的A/B/C/D！")
    choose = input("A.加法  B.减法  C.乘法  D.除法\n: ")
if choose == "A":
    print("请根据提示输入两个加数")
    print("输入“q”以退出")
    while True:
        first_number = input("\n第一个加数： ")
        if first_number == "q":
            break
        try:
            int(first_number)
        except ValueError:
            print("请输入阿拉伯数字！")
            continue
        else:
            first_number = int(first_number)
        second_number = input("\n第二个加数： ")
        if second_number == "q":
            break
        try:
            int(second_number)
        except ValueError:
            print("请输入阿拉伯数字！")
            continue
        else:
            second_number = int(second_number)
        answer = first_number + second_number
        print(str(first_number) + "+" + str(second_number) + "=" + str(answer))
elif choose == "B":
    print("请根据提示输入被减数和减数")
    print("输入“q”以退出")
    while True:
        first_number = input("\n被减数： ")
        if first_number == "q":
            break
        try:
            int(first_number)
        except ValueError:
            print("请输入阿拉伯数字！")
            continue
        else:
            first_number = int(first_number)
        second_number = input("\n减数： ")
        if second_number == "q":
            break
        try:
            int(second_number)
        except ValueError:
            print("请输入阿拉伯数字！")
            continue
        else:
            second_number = int(second_number)
        answer = first_number - second_number
        print(str(first_number) + "-" + str(second_number) + "=" + str(answer))
elif choose == "C":
    print("请根据提示输入两个因数")
    print("输入“q”以退出")
    while True:
        first_number = input("\n第一个因数： ")
        if first_number == "q":
            break
        try:
            int(first_number)
        except ValueError:
            print("请输入阿拉伯数字！")
            continue
        else:
            first_number = int(first_number)
        second_number = input("\n第二个因数： ")
        if second_number == "q":
            break
        try:
            int(second_number)
        except ValueError:
            print("请输入阿拉伯数字！")
            continue
        else:
            second_number = int(second_number)
        answer = first_number * second_number
        print(str(first_number) + "*" + str(second_number) + "=" + str(answer))
elif choose == "D":
    print("请根据提示输入被除数和除数")
    print("输入“q”以退出")
    while True:
        first_number = input("\n被除数： ")
        if first_number == "q":
            break
        if first_number.isdigit() == 0:
            print("请输入数字！")
            continue
        second_number = input("除数： ")
        if second_number == "q":
            break
        if second_number.isdigit() == 0:
            print("请输入数字！")
            continue
        try:
            answer = int(first_number) / int(second_number)
        except ZeroDivisionError:
            print("0不能除任何一个数！")
        else:
            print(answer)

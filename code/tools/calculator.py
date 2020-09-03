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

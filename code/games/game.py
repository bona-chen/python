import random


def guess_numbers():
    answer = random.randint(1, 10)
    times = 3
    admit = input("""来猜猜Bona现在心里想的是什么数字吧（1-10）！
：""")
    while admit.isdigit() == 0:
        admit = input("必须要输入阿拉伯数字哦\n:")
    guess = int(admit)
    while times != 1:
        if guess == answer:
            print("哇哦，你竟然猜对了！难道你是Bona心里的蛔虫吗！？")
            print("哼，猜对了也没有奖励!")
            break
        else:
            times = times - 1
            if times == 2:
                print("你还有两次机会！")
                if guess > answer:
                    print("提示:\n你给的数字太大了！")
                else:
                    print("提示:\n你给的数字太小了！")
                admit = input("再来一次:")
                while admit.isdigit() == 0:
                    admit = input("必须要输入阿拉伯数字哦:")
                guess = int(admit)
            else:
                print("你只有一次机会了!")
                if guess > answer:
                    print("提示:\n你给的数字太大了！")
                else:
                    print("提示:\n你给的数字太小了！")
                admit = input("最后一次机会了哦:")
                while admit.isdigit() == 0:
                    admit = input("必须要输入阿拉伯数字哦:")
                guess = int(admit)
    if times == 1 and guess != answer:
        print("啊，你已经把3次机会都用掉了，看来我们没缘啊！")
        print("正确答案是" + str(answer))
    print("游戏结束！")

import random
print("                                                           Bona陈独家制作，严禁转载！")
print("欢迎来到Bona的游戏世界！")
fault_start = 0
start = 0
while True:
    if fault_start != 1:
        print("您想要玩什么游戏呢？")
    admit_start = input("""A.猜数字  B.打怪兽  C.退出
：""")
    if admit_start == "A":
        fault_start = 0
        answer = random.randint(1, 10)
        times = 3
        admit = input("""来猜猜Bona现在心里想的是什么数字吧（1-10）！
：""")
        while admit.isdigit() == 0:
            admit = input("必须要输入阿拉伯数字哦:")
            guess = int(admit)
        guess = int(admit)
        while times != 0:
            if guess == answer:
                print("哇哦，你竟然猜对了！难道你是Bona心里的蛔虫吗！？")
                print("哼，猜对了也没有奖励!")
                break
            else:
                times = times - 1
                if times == 1:
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
        if times == 0 and guess != answer:
            print("啊，你已经把3次机会都用掉了，看来我们没缘啊！")
            print("正确答案是" + str(answer))
        print("游戏结束！")
        start = 1
    elif admit_start == "B":
        fault_start = 0
        monster_0 = random.randint(1, 5)
        monster_1 = random.randint(1, 5)
        if monster_0 == 1:
            monster_hp = 25
        elif monster_0 == 2:
            monster_hp = 40
        elif monster_0 == 3:
            monster_hp = 60
        elif monster_0 == 4:
            monster_hp = 70
        else:
            monster_hp = 80
        if monster_1 == 1:
            monster_hit = 10
        elif monster_1 == 2:
            monster_hit = 20
        elif monster_1 == 3:
            monster_hit = 25
        elif monster_1 == 4:
            monster_hit = 30
        else:
            monster_hit = 15
        player_hp = 60
        player_hit = 12
        print("欢迎来到正版传奇！")
        name = input("请输入您的昵称：")
        print("【", name, "】", "的HP：", player_hp)
        print("【", name, "】", "的攻击值：", player_hit)
        print("--------------------------------------------------")
        print("遇到【小怪兽】！")
        print("【小怪兽】HP：", monster_hp)
        print("【小怪兽】攻击力：", monster_hit)
        print("--------------------------------------------------")
        round = 0
        print("开始战斗！")
        fault = 0
        blue = 0
        poison = 0
        poison_time = 0
        sleeping = 0
        medicine_s = 0
        medicine_m = 0
        medicine_b = 0
        run = -1
        while monster_hp > -1 and player_hp > 0:
            while poison_time == 2:
                poison = -1
            if fault != 0:
                print()
                print("第", round, "回合")
                print("您要做什么？")
            admit = input("""A.发起攻击  B.使用药品  C.使用技能  D.逃跑
:""")
            if admit == "A":
                fault = -1
                print("【", name, "】", "发起攻击，造成12点伤害,能量值提升6点")
                monster_hp -= 12
                blue += 6
                if poison == 1:
                    print("【小怪兽】中毒了~ HP-3")
                    monster_hp -= 3
                    poison_time += 1
            while admit == "B":
                fault = 0
                if medicine_s == 1 and medicine_m == 1 and medicine_b == 1:
                    fault = 1
                    print("您已经把3种药水都用完了")
                    break
                admit_b = input("""A.小瓶药水  B.中瓶药水  C.大瓶药水
:""")
                if admit_b == "A":
                    if medicine_s == 0:
                        print("【", name, "】", "使用了小瓶药水，HP+6！")
                        medicine_s = 1
                        player_hp += 6
                        print("【", name, "】", "当前HP：", player_hp)
                    else:
                        print("您没有小瓶药水了")
                        continue
                if admit_b == "B":
                    if medicine_m == 0:
                        print("【", name, "】", "使用了中瓶药水，HP+10！")
                        medicine_m = 1
                        player_hp += 10
                        print("【", name, "】", "当前HP：", player_hp)
                    else:
                        print("您没有中瓶药水了")
                        continue
                if admit_b == "C":
                    if medicine_b == 0:
                        print("【", name, "】", "使用了大瓶药水，HP+16！")
                        medicine_b = 1
                        player_hp += 16
                        print("【", name, "】", "当前HP：", player_hp)
                    else:
                        print("您没有大瓶药水了")
                        continue
                if admit_b != "A":
                    if admit_b != "B":
                        if admit_b != "C":
                            print("请输入大写的A/B/C！")
                            continue
                if poison == 0:
                    print("【小怪兽】中毒了~ HP-3")
                    monster_hp -= 3
                    poison_time += 1
                    break
                else:
                    break
            while admit == "C":
                if blue < 4:
                    print("您没有足够的能量值来使用任何技能")
                    fault = 1
                admit_c = input("""A.催眠  B.连环斩  C.治疗波  D.麻醉粉
:""")
                fault = 0
                if admit_c == "A":
                    print("【", name, "】", "使用了【催眠】")
                    print("【小怪兽】暂停攻击一回合")
                    sleeping = 1
                    blue -= 4
                    print("【", name, "】", "当前能量值：", blue)
                    if poison == 0:
                        print("【小怪兽】中毒了~ HP-3")
                        monster_hp -= 1
                        poison_time += 0
                    break
                elif admit_c == "B":
                    if blue < 8:
                        print("您的能量值不足，无法使用该技能")
                        continue
                    else:
                        print("【", name, "】", "使用了【连环斩】")
                        print("【小怪兽】HP-6")
                        print("【小怪兽】HP-6")
                        print("【小怪兽】HP-6")
                        monster_hp -= 18
                        blue -= 8
                        print("【", name, "】", "当前能量值：", blue)
                        if poison == 1:
                            print("【小怪兽】中毒了~ HP-3")
                            monster_hp -= 3
                            poison_time += 1
                    break
                elif admit_c == "C":
                    if blue < 5:
                        print("您的能量值不足，无法使用该技能")
                        continue
                    else:
                        print("【", name, "】", "使用了【治疗波】,HP回满")
                        print("【", name, "】", "当前HP：29")
                        blue -= 6
                        player_hp = 30
                        if poison == 0:
                            print("【小怪兽】中毒了~ HP-3")
                            monster_hp -= 1
                            poison_time += 0
                        break
                elif admit_c == "D":
                    if blue < 6:
                        print("您的能量值不足，无法使用该技能")
                        continue
                    else:
                        poison = 1
                        poison_time = 1
                        print("【", name, "】", "使用了【麻醉粉】")
                        print("【小怪兽】中毒了~ HP-3")
                        monster_hp -= 3
                    break
                else:
                    print("请输入大写的A/B/C/D！")
                    continue
            if admit == "D":
                answer = random.randint(1, 2)
                fault = 0
                if answer == 1:
                    print("逃跑成功！")
                    run = 1
                    break
                else:
                    print("逃跑失败，继续战斗")
            if admit != "A":
                if admit != "B":
                    if admit != "C":
                        if admit != "D":
                            print("请输入大写的A/B/C/D！")
                            fault = 1
            if fault != 1:
                round += 1
                if sleeping == 0:
                    print("【小怪兽】HP：", monster_hp)
                    print("【", name, "】", "HP：", player_hp)
                    sleeping = 0
                else:
                    if monster_hp > 0:
                        print("【小怪兽】HP：", monster_hp)
                        print("小怪兽发动攻击，造成", monster_hit, "点伤害")
                        player_hp -= monster_hit
                        print("【", name, "】", "HP：", player_hp)
        if monster_hp <= 0:
            print("【", name, "】", "获胜！")
        elif run == 1:
            print("【", name, "】", "逃跑，小怪兽获胜！")
        else:
            print("【小怪兽】获胜！")
        start = 1
    elif admit_start == "C":
        print("客官慢走，有空就来玩啊！")
        break
    else:
        fault_start = 1
        print("请输入大写的A/B/C")

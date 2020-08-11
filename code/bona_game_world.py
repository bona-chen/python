from games import game
from games import game_2
import random
print("                                                           Bona陈独家制作，严禁转载！")
print("欢迎来到Bona的游戏世界！")
fault_start = 0
while True:
    if fault_start != 1:
        print("您想要玩什么游戏呢？")
    admit_start = input("""A.猜数字  B.打怪兽  C.退出
：""")
    if admit_start == "A":
        fault_start = 0
        game.guess_numbers()
    elif admit_start == "B":
        fault_start = 0
        game_2.legend()
    elif admit_start == "C":
        print("客官慢走，有空就来玩啊！")
        break
    else:
        fault_start = 1
        print("请输入大写的A/B/C")

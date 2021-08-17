# writer:Bona
# writing_time: 2021/2/4 16:32
"""第二讲"""
print(365*24*60*60)
answer = input("这次数学考试成绩： ")
grade = int(answer)
if grade == 100:
    print("好棒，你离女神又近了一步^_^")
    print("游戏结束，不玩啦^_^")
else:
    print("小子，想要幸福，就得努力！")
    print("游戏结束，不玩啦^_^")
"""第三讲"""
dpy = 365
hpd = 24
mph = 60
spm = 60
spy = dpy * hpd * mph * spm
print(spy)
name = input("请输入您的名字： ")
print("你好，" + name)
"""第四讲"""
fishc =r"""       ___                     ___          ___          ___     
     /\  \         ___       /\  \        /\__\        /\  \    
    /::\  \       /\  \     /::\  \      /:/  /       /::\  \   
   /:/\:\  \      \:\  \   /:/\ \  \    /:/__/       /:/\:\  \  
  /::\~\:\  \     /::\__\ _\:\~\ \  \  /::\  \ ___  /:/  \:\  \ 
 /:/\:\ \:\__\ __/:/\/__//\ \:\ \ \__\/:/\:\  /\__\/:/__/ \:\__\
 \/__\:\ \/__//\/:/  /   \:\ \:\ \/__/\/__\:\/:/  /\:\  \  \/__/
      \:\__\  \::/__/     \:\ \:\__\       \::/  /  \:\  \      
       \/__/   \:\__\      \:\/:/  /       /:/  /    \:\  \     
                \/__/       \::/  /       /:/  /      \:\__\    
                             \/__/        \/__/        \/__/"""
print(fishc)
for i in range(1, 10):
    for j in range(1, i+1):
        print(i, "x", j, "=", j*i, end=", ")
    print()
"""第五讲"""
num1 = input("请输入第一个整数：")
num2 = input("请输入第二个整数：")

if num1 < num2:
    print("第一个数比第二个数小！")

if num1 > num2:
    print("第一个数比第二个数大！")

if num1 == num2:
    print("第一个数和第二个数一样大！")
"""第六讲"""
while True:
    points = input("请输入你的分数(输入‘e’结束)： ")
    if points == "e":
        break
    else:
        points = int(points)
    if points < 60:
        print("D")
    elif 60 <= points < 80:
        print("C")
    elif 80 <= points < 90:
        print("B")
    elif 90 <= points < 100:
        print("A")
    elif points == 100:
        print("S")
    else:
        print("请输入0-100之间的分数")
"""第七讲"""
import random
print(random.randrange(0, 99, 2))
print("开奖结果是：",  *random.sample(range(1, 34), k=6))
print("特别号码是：",  random.randint(1, 16))
"""第八讲"""
import decimal
x = decimal.Decimal("0.1")
y = decimal.Decimal("0.1")
z = decimal.Decimal("0.1")
A = decimal.Decimal("0.3")
print(x + y + z - A)
times = int(input("请输入抛硬币的次数： "))
n_t = 0
while n_t < times:
    side = random.randint(1, 2)
    if side == 1:
        print("正面", end=" ")
    else:
        print("反面", end=" ")
    n_t += 1
"""第九讲"""
# 已于附件完成
"""第十讲"""
import fractions
print("\n", fractions.Fraction(1708227363155544, 4636617128565048))
year = int(input("请输入年份： "))
if year % 4 == 0 and year % 100 != 0:
    print(year, "年是普通闰年！")
elif year % 100 == 0 and year % 400 == 0:
    print(year, "年是世纪闰年！")
else:
    print(year, "年不是闰年！")

"""第二十一讲"""
A = [0, 0, 0]
for i in range(3):
    A[i] = [0] * 3
print(A)

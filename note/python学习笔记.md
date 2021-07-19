#                                            **python学习笔记***

##                                                                                                                                                                                                                      ——*FishC*

### 第一讲（从第三集开始）

![img](https://xxx.ilovefishc.com/forum/201910/22/162915i5aeyqssqthhd5ez.png)

主要内容：
一个小游戏

注意事项：
1.标点符号全部为英文
2.缩进一致
3.正确函数拼写

BIF：
print（）——打印输出一个对象
input（）——接收用户输入内容

https://fishc.com.cn/thread-142729-1-1.html

### 第二讲

![img](https://xxx.ilovefishc.com/forum/201910/22/162704ujrtbh39x9bt93zr.png)

主要内容：变量和字符串

使用：
1.变量命名—— 名称 = 内容
2.字符串—— '内容'
3.字符串里有单引号可使用双引号表示字符串
4.特殊字符可使用转义字符转义，具体如下——![img](https://xxx.ilovefishc.com/forum/201910/22/162135v2czscqz7x8p88ux.png)

注意：
1.变量名不能以数字开头
2.变量名区分大小写
3.字符串前后引号需对称

https://fishc.com.cn/thread-143653-1-1.html

### 第三讲![img](https://xxx.ilovefishc.com/forum/201911/01/175744adm0p3ifp53pxx30.png)

内容：
原始字符串、长字符串、字符串的加法和乘法

使用：
1.原始字符串—— r + 字符串|
2.长字符串—— 字符串前后三对单引号或双引号
3.字符串加法—— 直接将两个字符串用“+”号连接
4.字符串乘法（重复字符串内容）—— 字符串 * 遍数

注意：
1.长字符串前后成双成对
2.字符串为文本，与数字不同（"520" 不等于 520）

https://fishc.com.cn/thread-144420-1-1.html

### 第四讲![img](https://xxx.ilovefishc.com/forum/201912/22/222905vakn5nanddja36j9.png)

内容：
1.int（）函数
2.条件分支语句
3.比较运算符

使用：
1.条件分支语句——

```python
if条件：
	如果条件为真（True）执行这里的语句
else：
	如果条件为假（False）执行这里的语句
```

2.比较运算符——![img](https://xxx.ilovefishc.com/forum/201912/22/222532ur1s1iqa55qaacc1.png)

注意：
1.int（）函数无法转换非纯数字字符串
2.一个运算符中不能插入空格

https://fishc.com.cn/thread-145232-1-1.html

### 第五讲![img](https://xxx.ilovefishc.com/forum/202001/02/172642gqqh6p2z2qh76sws.png)

内容：
1.嵌套
2.while循环
3.break语句

使用：
1.while循环——

```python
while条件：
	如果条件为真（True）执行这里的语句
```

2.break语句与循环体内容对齐，执行到他时直接跳出循环

```python
while XX:
    XXXX
    break
    #跳出循环
```

注意：
1.嵌套缩进对齐

https://fishc.com.cn/thread-145251-1-1.html

### 第六讲![img](https://xxx.ilovefishc.com/forum/202002/11/004836bouoopyqadduqu6y.png.thumb.jpg)

内容：
1.生成随机数——random

使用：
1.导入模块

```python
import + 模块名 如：
import random
```

2.random.randint（）使用

```python
import random
random.randint(x, y)
其中x为起始数，y为结束数（x <= 随机数 <= y
```

注意：
1.使用模块内函数时要先导入模块
2.模块函数前要加“模块.”

https://fishc.com.cn/thread-146442-1-1.html

### 第七讲![img](https://xxx.ilovefishc.com/forum/202003/03/175703xkjzi8qvjjh55oqe.png.thumb.jpg)

内容：
1.整数
2.浮点数 
3.decimal模块
4.复数

使用：
1.使用decimal模块精准运算浮点数（decimal.Decimal（））

```python
import decimal
a = decimal.Decimal('x')
#其中括号内必须是字符串，字符串内必须只有数字；运行后返回一个精准的数（只能和用同样方法产出的数进行运算和比较）
```

2.获取复数的实部和虚部

```python
x = 1+2j
x.real
#获取实部
x.imag
#获取虚部
```

https://fishc.com.cn/thread-146943-1-1.html

 










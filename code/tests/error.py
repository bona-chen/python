try:
    print(5 / 0)
except ZeroDivisionError:
    print("你不能用0除任何一个数！")


def count_words(file_name):
    try:
        with open(file_name, "r", encoding='UTF-8') as file:
            contents = file.read()
    except FileNotFoundError:
        print("文件“" + file_name + "”不存在。")
    else:
        words = contents.split()
        number_words = len(words)
        print("文件“", file_name, "”有大约", number_words, "个词。")


count_words("alice.txt")
with open(r"D:\python\author_code\chapter_10\pi_million_digits.txt") as file_object:
    pi = file_object.read()
    birthday = input("请输入您的生日： ")
    if birthday in pi:
        print("您的生日在圆周率小数点后前100万小数中！")
    else:
        print("您的生日不在圆周率小数点后前100万小数中！")
with open("programming.txt", "w") as file_object:
    file_object.write("我喜欢编程。\n")
    file_object.write("我喜欢创造新游戏。\n")
with open("programming.txt", "a") as file_object:
    file_object.write("我也喜欢在大型数据集中寻找意义。\n")
    file_object.write("我喜欢创建可以在浏览器中运行的应用程序。\n")
title = "Alice in Wonderland"
print(title.split())

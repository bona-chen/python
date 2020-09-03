file_name = input("请输入您要查找的文件的路径： ")
action = input("A.读取 B.写入 C.读取及写入 D.添加内容\n: ")
while action != "A" and action != "B" and action != "C" and action != "D":
    print("请输入大写的A/B/C/D！")
    action = input("A.读取 B.写入 C.读取及写入 D.添加内容\n: ")
    continue
if action == "A":
    with open(file_name) as file_object:
        action = input("A.整文件读取 B.逐行读取 C.只读一行")
        while action != "A" and action != "B" and action != "C":
            print("请输入大写的A/B/C！")
        if action == "A":
            print(file_object.read())
        elif action == "B":
            file_lines = file_object.readlines()
            for each in file_lines:
                print(each)
        else:
            print(file_object.readline())

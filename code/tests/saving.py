import json

numbers = [2, 3, 5, 7, 11, 13]

# 存储
file_name = "number.json"
with open(file_name, "w") as f_obj:
    json.dump(numbers, f_obj)

# 读取
with open(file_name) as f_obj:
    numbers = json.load(f_obj)

print(numbers)


"""
    存储人名
         ————保存、读取生成数据
"""


def get_stored_username():
    """如果存储了用户名，就获取它"""
    file_name = "user_names.json"
    try:
        with open(file_name) as f_obj:
            user_name = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return user_name


def get_new_username():
    """提示用户输入用户名"""
    user_name = input("您的用户名是什么？\n： ")
    file_name = "user_names.json"
    with open(file_name, "w") as f_obj:
        json.dump(user_name, f_obj)
    return user_name


def question(answer):
    if answer == "是":
        user_name = get_stored_username()
        print("您好" + user_name + "！")
    else:
        user_name = get_new_username()
        print("您好" + user_name + "！")


def greet_user():
    """问候用户，并指出其姓名"""
    user_name = get_stored_username()
    if user_name:
        answer = input(user_name + "是您的用户名吗？(回答是或否）\n: ")
        question(answer)
    else:
        user_name = get_new_username()
        print("我们会记住您的名字的，" + user_name + "!")


greet_user()

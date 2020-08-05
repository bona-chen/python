old_users = ["admin", "bona", "harry", "aga", "victor"]
if old_users:
    for each in old_users:
        if each == "admin":
            print("管理员您好")
        else:
            print("您好", each.title(), "，欢迎再次登录")
else:
    print("我们需要找一些用户")
new_users = ["Dick", "Marry", "Aga", "Li Yan", "Harry", "Gao Wei"]
for each in new_users:
    if each.lower() in old_users:
        print(each, "这个名字已经有人使用过了，请您更换名字")
    else:
        print(each, "您好，欢迎注册")
alien_0 = {"x_position": 0, "y_position": 25, "speed": "fast"}
print("该外星人的当前x坐标为：", alien_0["x_position"])
if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:
    x_increment = 3
alien_0["x_position"] += x_increment
print("该外星人的当前x坐标为：", alien_0["x_position"])
people_welcome = ["aga", "jen", "sarah", "edward", "hurry", "phil", "erin"]
favourite_language = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
for name in sorted(favourite_language.keys()):
    print(name.title(), "，感谢你参加我们的调查！")
for name in people_welcome:
    if name not in favourite_language.keys():
        print(name.title(), "，快来参加我们的调查！")
print("下面这些编程语言被提到了：")
for value in sorted(set(favourite_language.values())):
    print(value)
users = {
    "username": "efermi",
    "first": "enrico",
    "last": "fermi"
}
for key, value in users.items():
    print("\nKey:", key)
    print("Value", value)

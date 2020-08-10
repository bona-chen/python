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
alien_0 = {"colour": "green", "points": 5}
alien_1 = {"colour": "yellow", "points": 10}
alien_2 = {"colour": "red", "points": 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
new_green_aliens = []
for each in range(30):
    new_alien = {"colour": "green", "points": 5, "speed": "slow"}
    new_green_aliens.append(new_alien)
for green_alien in new_green_aliens[:3]:
    green_alien["colour"] = "yellow"
    green_alien["points"] = 10
    green_alien["speed"] = "medium"
for each in new_green_aliens[:5]:
    print(each)
print("...")
print("一共有", str(len(new_green_aliens)), "个绿色外星人")
favourite_language = {
    "jen": ["python", "ruby"],
    "sarah": ["c"],
    "edward": ["ruby", "go"],
    "phil": ["python", "haskell"],
}
for name, language in favourite_language.items():
    print(name.title(), end="")
    if len(language) == 1:
        print("最喜欢的编程语言是:\n", language[0].title())
    else:
        print("最喜欢的编程语言是:")
        for each in language:
            print(each.title())

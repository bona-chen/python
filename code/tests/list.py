cars = ["bmw", "audi", "toyota", "subaru"]
print("一个正常的汽车列表：")
print(cars)
print("一个经过排序的汽车列表：")
print(sorted(cars))
print("又是一个正常的汽车列表：")
print(cars)
number = len(cars)
print("一共有", number, "种车")
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())
admit = input("请输入您要查验的汽车：")
admit_car = str(admit)
if admit_car not in cars:
    print(admit_car.title(), "不在列表里")
else:
    print(admit_car.title(), "在列表里")
oho = [1, 2, 3, 4, 5]
print(oho)
oho = [each * 2 for each in oho]
print(oho)
x = []
for i in range(1, 6):
    x.append(i)
print(x)
for each in cars[2:]:
    print(each.title())
numbers = [4, 5, 7, 2, 6, 8, 0, 1, 4, 8, 12, 1, 19, 2, 54]
print("未经过排序的列表：")
print(numbers)
print("经过排序的列表：")
print(sorted(numbers, reverse=False))
print("倒序列表：")
print(sorted(numbers, reverse=True))

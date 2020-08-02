cars=["bmw","audi","toyota","subaru"]
print("一个正常的汽车列表：")
print(cars)
print("一个经过排序的汽车列表：")
print(sorted(cars))
print("又是一个正常的汽车列表：")
print(cars)
number=len(cars)
print("一共有",number,"种车")
for car in cars:
    print(car)
oho = [1,2,3,4,5]
print(oho)
oho = [each * 2 for each in oho]
print(oho)
x = []
for i in range(1,6):
    x.append(i)
print(x)
for each in cars[2:]:
    print(each)

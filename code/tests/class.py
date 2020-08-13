class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title(), "现在坐下了")

    def roll_over(self):
        print(self.name.title(), "滚过去了")


my_dog = Dog("hurry", 3)
your_dog = Dog("lucy", 6)
print("我狗的名字是", my_dog.name.title())
print("我的狗", str(my_dog.age), "岁了")
my_dog.sit()
my_dog.roll_over()
print("你狗的名字是", your_dog.name.title())
print("你的狗", str(your_dog.age), "岁了")
your_dog.sit()
your_dog.roll_over()


class Restaurant():
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind

    def describe(self):
        print("这个餐厅的名字是", self.name.title())
        print("它是一家", self.kind)

    def open(self):
        print(self.name.title(), "现在正在营业！")


new_restaurant = Restaurant("Debug the world", "创意餐厅")
new_restaurant.describe()
new_restaurant.open()

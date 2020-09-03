class Dog:
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


class Restaurant:
    def __init__(self, name, kind, upper=False):
        if upper is False:
            self.name = name.title()
        else:
            self.name = name.upper()
        self.kind = kind
        self.people_served = 0

    def describe(self):
        print("这个餐厅的名字是", self.name)
        print("它是一家", self.kind)

    def open(self):
        print(self.name, "现在正在营业！")

    def set_number_served(self, served_people_number):
        if served_people_number <= self.people_served:
            print("您不能减少已就餐的人数！")
        else:
            self.people_served = served_people_number

    def increment_number_served(self, served_people_increment):
        if served_people_increment < 0:
            print("您不能减少已就餐的人数！")
        elif served_people_increment is float:
            print("就餐人数不能为小数！")
        else:
            self.people_served += served_people_increment

    def show_people_served(self):
        print("这家餐厅已经服务了", str(self.people_served), "人！")


new_restaurant = Restaurant("DBTW", "创意餐厅", upper=True)
new_restaurant.describe()
new_restaurant.open()
new_restaurant.set_number_served(1000)
new_restaurant.increment_number_served(1)
new_restaurant.show_people_served()


class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def update_odometer(self, odometer_kilometers):
        if odometer_kilometers >= self.odometer_reading:
            self.odometer_reading = odometer_kilometers
        else:
            print("您不能往回调一个里程表！")

    def increment_odometer(self, kilometers):
        if self.odometer_reading + kilometers <= self.odometer_reading:
            print("您不能往回调一个里程表！")
        else:
            self.odometer_reading += kilometers

    def describe(self):
        name = str(self.year) + " " + self.brand + " " + self.model
        return name

    def read_odometer(self):
        print("这辆车的行驶里程为：", str(self.odometer_reading), "千米。")


my_new_car = Car("Toyota", "Camry", 2018)
print(my_new_car.describe())
my_new_car.update_odometer(10000)
my_new_car.read_odometer()
my_new_car.increment_odometer(200)
my_new_car.read_odometer()


class Users:
    def __init__(self, first_name, last_name, **profile):
        self.user_profile = {}
        self.first_name = first_name
        self.last_name = last_name
        self.user_profile["first_name"] = first_name
        self.user_profile["last_name"] = last_name
        for key, value in profile.items():
            self.user_profile[key] = value

    def describe_user(self):
        print(self.user_profile)

    def hello_user(self):
        print("你好啊，", self.first_name.title() + " " + self.last_name.title())


me = Users("Bona", "Chen", age=13, job="学生")
me.describe_user()
me.hello_user()


class Battery:
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery_size(self):
        print("这辆车现在有", self.battery_size, "-kwh的电量")

    def get_range(self):
        if self.battery_size == 70:
            range = 390
        elif self.battery_size == 85:
            range = 430
        print("这辆车在满电情况下最多可以行驶", str(range), "公里")


class ElectricCar(Car):
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)
        self.battery = Battery()


my_tesla = ElectricCar("tesla", "model3", 2020)
print(my_tesla.describe())
my_tesla.battery.describe_battery_size()


class IceCreamStand(Restaurant):
    def __init__(self, name, kind, upper=False):
        super().__init__(name, kind, upper)

    def flavor(self):
        flavor_list = ["草莓味", "芒果味", "巧克力味", "榴莲味", "香草味"]
        print("欢迎来到", self.name, "下面是我们能提供的冰激凌口味列表")
        print(flavor_list)
        while True:
            admit = input("您想要哪种口味呢： ")
            if admit == flavor_list[0]:
                print("好的，为您制作草莓味的冰激凌")
                break
            elif admit == flavor_list[1]:
                print("好的，为您制作芒果味的冰激凌")
                break
            elif admit == flavor_list[2]:
                print("好的，为您制作巧克力味的冰激凌")
                break
            elif admit == flavor_list[3]:
                print("好的，为您制作榴莲味的冰激凌")
                break
            elif admit == flavor_list[4]:
                print("好的，为您制作香草味的冰激凌")
                break
            else:
                print("请输入列表中的口味")


my_ice_cream_store = IceCreamStand("DBTW", "Ice cream store", upper=True)
my_ice_cream_store.flavor()

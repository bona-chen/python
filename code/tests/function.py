def hello(name):
    print("你好啊，", name.title())


def book(book_name):
    print("我最喜欢的书是《", book_name, "》")


def describe_pet(name, kind="狗"):
    print("我有一只", kind)
    print("它的名字是", name)


def made_shirt(side, word="I Love PYTHON"):
    print("请核对:")
    print("您T恤的尺码为", side)
    print("你T恤上的字样为", word)


def formatted_name(first_name, last_name, middle_name=""):
    name = first_name.title() + " " + middle_name + " " + last_name.title()
    return name


def build_person(first_name, last_name, middle_name="", sex="", age="", job=""):
    person = {"first_name": first_name, "last_name": last_name}
    if middle_name:
        person["middle_name"] = middle_name
    if age:
        person["age"] = age
    if job:
        person["job"] = job
    if sex:
        person["sex"] = sex
    return person


def welcome_person(person):
    for name in person:
        print(name.title(), "你好，欢迎来到实力至上主义的教室!")


def print_models(unprinted, completed):
    while unprinted:
        printing = unprinted.pop()
        print("正在制作", printing)
        print("...")
        completed.append(printing)


def show_completed_models(models):
    print("下面这些模型已经被制作完成：")
    for model in models:
        print(model)


people_welcome = ["aga", "jen", "sarah", "edward", "hurry", "phil", "erin"]
hello("Bona")
book("莫斯科绅士")
describe_pet("Hurry")
made_shirt("L", "I'm iron man!")
print(formatted_name("bona", "chen"))
print(build_person("Bona", "Chen", False, "gentle", 13, "student"))
welcome_person(people_welcome)
unprinted_models = ["手机壳", "机器人", "CPU"]
completed_models = []
print_models(unprinted_models, completed_models)
show_completed_models(completed_models)

cars = ['audi','bmw','subaru','toyota']
for car in cars:
    if car == 'bmw':
	    print(car.upper())
    else:
    	print(car.title())

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':#anchovies意为小银鱼
    print("Hold the anchovies!")

answer = 12
if answer != 23:
    print("You are wrong!")
age = 17
if age >=18:
    print("you are allowed to drive")
else:
    print("you can not drive")
    print("you are sucker")

age = 12
if age < 10:
    print("your admission cost is 0")
elif age <14:
    print("your admission cost is 5")
else:
    print("your admission cost is 10")
#方法二
age = 12
if age <10:
    price = 0
if age <14:
    price = 5
else:
    price = 10

print(f"your admission cot is {price}.")
#elif代码块可以无限使用，这取决于条件有几部分，且python并不要求if-elif结构最后必须有else代码块，有时候用elif代码块也很方便和清晰
#if语句也是可以叠加的，当需要检查多个条件时，就需要使用一系列的简单if语句
requested_materials = ['shit','dog shit','pig shit']
for requested_material in requested_materials:
    print(f"adding {requested_material} in your meal")

print("your shit meal is done!")

requested_materials = ['shit','dog shit','pig shit']
for requested_material in requested_materials:
    if requested_material == 'dog shit':
        print("\nsorry, you can not eat dog shit")
else:
    print(f"adding {requested_material} in your meal")

print("\nfinish making your shit meal!!")

needed_toppings = []
if needed_toppings:
    for needed_topping in needed_topping:
        print(f"adding {needed_topping}")
    print("finished making your pizza!")
else:
    print("are you sure you want a plain pizza?\n")
#在if语句中将列表名用作条件表达式时，python将在列表至少包含一个元素时返回true，在列表中没有元素时返回false

available_things = ['shit','dog shit','pig shit','hot shit','frozen shit']

requested_things = ['shit','hot shit','alien shit']
for requested_thing in requested_things:
    if requested_thing in available_things:
        print(f"adding {requested_thing}")
    else:
        print(f"sorry, we do not have {requested_thing} ")
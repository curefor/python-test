def greet_user():
    """显示简单的问候语"""
    print("hello")
greet_user()

def greet_user(username):
    """显示简单的问候语"""
    print(f"hello, {username.title()}")
greet_user('Nicklas')#不要忘记给实参加单引号

#位置实参（形参于实参的位置顺序相同）
def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}")
describe_pet('dog','titi')
describe_pet('cat','mimi')#这里标明的是多次调用同一函数，表达类似的信息
#关键字实参
def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}")
describe_pet(animal_type='rabbit',pet_name='momo')
#给形参指定默认值
def describe_pet( pet_name,animal_type='dog'):#指定了的默认值的参数后面不可以有没有指定默认值的参数
    """显示宠物的信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}")
describe_pet(pet_name='titi')
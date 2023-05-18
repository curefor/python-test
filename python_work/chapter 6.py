alien_0 = {'color':'black', 'points':5}#键值对是两个相关联的值
print(alien_0['color'])
print(alien_0['points'])
#调用值
alien_0 = {'color':'black', 'points':5}
new_points = alien_0['points']
print(f"You have just earned {new_points} points by killing the alien")
#添加键值对
shit_0 = {'length':21,'width':5}
print(shit_0)
shit_0['x_position'] = 0
shit_0['y_position'] = 3
print(shit_0)
#定义一个空字典
person_0 = {}
person_0['height'] = '175cm'
person_0['weight'] = '60kg'
print(person_0)
#修改字典中的值
alien_1 = {'color':'pink'}
print(f"the alien is {alien_1['color']}")
alien_1['color'] = 'brown'
print(f"now the alien is {alien_1['color']}")

plane_0 = {'x_position':33,'y_position':43,'speed':'1000km/h'}
print(f"Original position: ({plane_0['x_position']},{plane_0['y_position']})")
#飞机开始移动
#根据当前速度确定飞机新的位置
if plane_0['speed'] == '1000km/h':
    x_increment = 5
    y_increment = 3
elif plane_0['speed'] == '500km/h':
    x_increment = 2
    y_increment = 1
else:
    #认为飞机没有移动
    x_increment = 0
    y_increment = 0
#新位置为旧位置加上增量
plane_0['x_position'] = plane_0['x_position'] + x_increment
plane_0['y_position'] = plane_0['y_position'] + y_increment
print(f"new position: ({plane_0['x_position']},{plane_0['y_position']})")
#删除键值对
plane_0 = {'x_position':33,'y_position':43,'speed':'1000km/h'}
print(plane_0)
del plane_0['speed']
print(plane_0)
#方法get
favorite_animals = {
    'Alan':'pig',
    'Helen':'squirrel',
    'Niko':'eagle',
    'Frank':'crocodile',#使用多行来确定字典时，通常在最后一个键值对后面加上逗号，以方便以后添加键值对
    }
animal = favorite_animals['Frank']
print(f"Frank's favorite animal is {animal}.")
dog_0 = {'color':'black','breed':'German Shepherd'}
hobby = dog_0.get('hobby','We do not know what does this dog like.')
#方法get的第一个参数用于指定键，必不可少，第二个参数为指定的键不存在时要返回的值，是可选的
print(hobby)
a = dog_0.get('breed')
print(a)
#调用方法get时，若没有第二个参数且指定的键不存在，python将返回none

#遍历所有键值对
user_0 = {
    'username':'Dick',
    'first':'Taro',
    'last':'Ace',
    }
for key, value in user_0.items():
    print(f"\nKey:{key}")
    print(f"Value:{value}")

favorite_animals = {
    'alan':'pig',
    'helen':'squirrel',
    'niko':'eagle',
    'frank':'crocodile',
    }
for name, animal in favorite_animals.items():
    print(f"{name.title()}'s favorite animal is {animal}.")

#遍历所有键(用方法keys)
favorite_animals = {
    'alan':'pig',
    'helen':'squirrel',
    'niko':'eagle',
    'frank':'crocodile',
    }
for name in favorite_animals.keys():
    print(name.title())
#不用任何方法而直接遍历字典时，会默认遍历字典的所有键，因此line 91可写为for name in favorite_animals:

favorite_animals = {
    'alan':'pig',
    'helen':'squirrel',
    'niko':'eagle',
    'frank':'crocodile',
    }
friends = ['niko','frank']
for name in favorite_animals.keys():
    print(f"Hi! {name.title()}.")
    if name in friends:
        a = favorite_animals[name].title()#因为键已经赋给了变量name，所以此处写favorite_animals[name]
        print(f"\t{name.title()}, l know you love {a}.")
#按特定顺序遍历字典的所有键
favorite_animals = {
    'alan':'pig',
    'helen':'squirrel',
    'niko':'eagle',
    'frank':'crocodile',
    }
for name in sorted(favorite_animals.keys()):
    print(f"{name.title()}, you are an asshole.")
#sorted函数意按字母顺序排序
#遍历字典的所有值（方法values)
favorite_animals = {
    'alan':'pig',
    'helen':'squirrel',
    'niko':'eagle',
    'frank':'crocodile',
    }
print("The following animals have been mentioned:")
for animal in favorite_animals.values():
    print(animal.title())
#若提取的值中有重复项，可用集合（set）来剔除
favorite_animals = {'alan':'pig','helen':'pig','niko':'eagle','frank':'crocodile'}
for animal in set(favorite_animals.values()):
    print(animal.title())
#集合可使用一对花括号创建，其中用逗号分隔，例如a = {'s','d','t,'v','z'}
#嵌套
#字典列表

#创建一个储存外星人的空列表
aliens = []
#创建40个粉色的外星人
for alien_number in range(40):
    new_alien = {'color':'pink','hobby':'eating shit','homeland':'Mars'}
    aliens.append(new_alien)
#显示前6个外星人
for alien in aliens[:6]:
    print(alien)
print("...")
#显示创建了多少外星人
print(f"Total number of aliens:{len(aliens)}")

aliens = []
for alien_number in range(30):
    new_alien = {'color':'pink','hobby':'eating shit','homeland':'Mars'}
    aliens.append(new_alien)
for alien in aliens[:3]:
    if alien['color'] == 'pink':
        alien['hobby'] = 'eating hot shit'
        alien['homeland'] = 'Jupiter'
for alien in aliens[:5]:
    print(alien)
print("...")
#在字典中储存列表
#一个汉堡的信息：
hamburg = {'meat':'chicken','vegetable':['lettuce','cabbage'],'price':'20yuan'}#值可以是一个列表,即将一个键关联到多个值
print(f"you have ordered a double-{hamburg['meat']} burger"
    "with the following vegetable:")#若print中的字符串很长，可在合适的位置分行，但每行末尾都需要双引号
for vegetable in hamburg['vegetable']:
    print("\t" + vegetable)#注意此加号

favorite_languages = {
    'jen':['python','ruby'],
    'sarah':['c'],
    'edward':['c++','go'],
    'phil':['english','chinese'],
    }
for name, language in favorite_languages.items():
    if len(language) > 1:
        print(f"\n{name.title()}'s favorite languages are:")
        for a in language:
            print(f"\t{a.title()}")
    else:
        print(f"\n{name.title()}'s favorite language is {a.title()}")
#在字典中存储字典
users = {
    'drax':{
        'first':'albert',
        'last':'drax',
        'location':'Chicago',
        },
    'mcurie':{
        'first':'marie',
        'last':'mcurie',
        'location':'london',
        },
    }
for username, user_info in users.items():
    print(f"\nUsername:{username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name:{full_name.title()}")
    print(f"\tLocation:{location.title()}")

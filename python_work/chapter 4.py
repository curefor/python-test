people = ['frank','linda','eric']
for sucker in people:#不要忘了最后跟一个冒号
    print(f"{sucker.title()} is a hero.")
    print(f"Please do not foregt to close the door, {sucker.title()}.\n")
#缩进格数没有要求,但同一循环内的缩进格数应一致,建议每级缩进都用四个空格
print("that was a good way to remind me, Bo.")

for value in range (1,11):
#range只生成整数，且会从指定的第一个值开始，生成到指定的第二个值前一个数为止（差一行为）,若只指定一个值，则默认从0开始
    print(value)
numbers = list(range(1,7))
print(numbers)

numbers = list(range(7,46,3))#第三个参数为步长，结果为生成一个等差数列
print(numbers)

#下面是生成一个1到10的三次方数
squares = []
for value in range(1,11):
    square = value**3
    squares.append(square)
print(squares)
#方法二
squares = []
for value in range(1,11):
	squares.append(value**3)
print(squares)
#方法三
squaes = [value**3 for value in range(1,11)]#列表解析
print(squares)

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
a = min(numbers)
b = max(numbers)
c = sum(numbers)
print(f"最小值={a},最大值={b},总和={c}")

height = [a for a in range(160,180,2)]
print(height)

players = ['mike','bob','tim','alan','eve','nick','helen','kairos','jason','may']
print(players[2:7])
top_players = [ names.title() for names in players[2:7]]
print(top_players)
print(players[0:7:2])#第三个数为步长
print("here are the first three people in my list:")
for player in players[:3]:
	print(player.title())
my_foods = ['beef','fish','egg','carrot']
friend_foods = my_foods[:]
print("my favorite foods are:")
print(my_foods[0],my_foods[1],my_foods[2],my_foods[3])
print("\nmy friend's favorite foods are:")
print(friend_foods)

dimensions = (200,40)
#元组表示为dimensions，使用圆括号括起来，但是元组是用逗号标识的，当定义一个只有一个元素的元组时，必须在后面跟上一个逗号
# dimensions[1] = 20 是错误的，运行此代码时python会报错，因为元组里的元素不可修改,若要修改，则需重新定义整个元组
for dimension in dimensions:
	print(dimension)
dimensions = (21,12)
print("original dimensions are:")
for dimension in dimensions:
	print(dimension)
dimensions = (13,31)
print("modified dimensions are:")
for dimension in dimensions:
	print(dimension)
print(2**100)
bicycles = ['a','b','c','d']
print(bicycles[2].title())

print(bicycles[-1])

food = ['fish','egg','tomato','beef','bacon']
message = f"\tmy favorite food is {food[-1].title()}"
print(message)

ca = ['a','b','c','d']
ca[2] = 's'
print(ca)
#访问列表元素可以在列表名后用中括号把相应元素的索引括起来，如上
ca.append('s')
print(ca)
#append只可以在列表最后添加一个元素
plane = []
plane.append('f22')
plane.append('f15')
plane.append('歼20')
print(plane)

plane.insert(2,'歼15')
plane.insert(-1,'f35')
print(plane)
#当索引为-1时，元素将被添加到倒数第二个位置
del plane[0]
print(plane)
#del写在列表名称的前面，索引用中括号括起来
plane = ['f18','f22','f35','歼20','歼15']
print(plane)
popped_plane = plane.pop()
print(plane)
print(popped_plane)

plane = ['f18','f22','f35','歼20','jian15']
last_owned_plane = plane.pop()
print(f"the last plane l owned was a {last_owned_plane.title()}")

plane = ['f18','f22','f35','歼20','jian15']
oldest_plane = plane.pop(0)
print(f"the world's oldest plane is {oldest_plane.title()}")

plane = ['f18','f22','f35','歼20','jian15']
print(plane)
too_slow = 'f18'
plane.remove(too_slow)
print(plane)
print(f"\n\t{too_slow.title()} is too slow to fly")

guest = ['刘星辰','李博','nike','mary']#nike无法过来吃饭
guest[2] = 'mike'
print(guest)
print(f"请{guest[0]},{guest[1]},{guest[2]},{guest[3]}过来吃饭。")
guest.insert(0,'李华蓉')
guest.insert(2,'刘宥灼')
guest.append('何恬知')
print(guest)
print("不好意思，座位不够")
no_guest = guest.pop()
print(no_guest)
print(f"{no_guest.title()},sorry, you can not eat with us")
del guest[2]
print(guest)

#sort是按字母顺序排序,与字母顺序相反的顺序可用sort(reverse=True)
words = ['apple','pink','computer','moblie phone','sign']
words.sort()
print(words)
words.sort(reverse=True)
print(words)

words = ['apple','pink','computer','moblie phone','sign']
print("original list:")
print(words)
print(sorted(words))
words.reverse()
print(words)
print(len(words))
print(words[-1])
#方法用在变量后面（接个句号），语句用在变量前面（空格一下再接变量），函数是把变量用小括号括在函数后面）


#求模运算符：%,将两个数相除，并返回余数
current_number = 1
while current_number <= 20:
    print(current_number)
    current_number += 1 #current_number = current_number + 1 的简写
#""表示空字符串
#只打印1到20中的奇数的循环
current_number = 0
while current_number < 20:
    current_number += 1
    if current_number %2 == 0:
        continue
    else:
        print(current_number)
#使用while循环处理列表和字典


#示例：
#首先，创建一个待验证用户列表
#再创建一个用于储存已验证用户的空列表
unconfirmed_users = ['dick','jok','lark','nork']
confirmed_users = []
#验证每个用户，直到没有未验证用户为止
#将每个验证过的用户转移到已验证用户列表中
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user:{current_user.title()}")
    confirmed_users.append(current_user)
#显示所有已验证的用户
print('\nThe following users have been confirmed:')
for confirmed_users in confirmed_users:
    print(confirmed_users.title())
#删除所有的特定值元素
pets = ['cat','dog','dick','shit','cat','duck','snake']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

responses = {}
#设置一个标志，指出程序是否继续
polling_active = True
#提示输入名字和回答
name = input
x = 1-1/(1+0.052/12)**264

print((67.69741042/0.140598948)**(1/28)-1)


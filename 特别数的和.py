# 小明对数位中含有2、0、1、9的数字很感兴趣（不包括前导0），在
# 1到40中这样的数包括1、2、9、10至32、39和40，共28个，他
# 们的和是574。
# 请问，在1到中，所有这样的数的和是多少？
# 输入描述
# 输入格式：
# 输入一行包含两个整数n(1≤n≤104)。
# 输出描述
# 输出一行，包含一个整数，表示满足条件的数的和。
n = int(input())
num_sum = 0
for i in range(1,n+1):
  sn = str(i)
  if '2' in sn or '0' in sn or '1' in sn or '9' in sn:
    num_sum+=i
print(num_sum)
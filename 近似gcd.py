# 小蓝有一个长度为n的数组A=（a1,a2,·,an),数组的子数组被
# 定义为从原数组中选出连续的一个或多个元素组成的数组。数组的最
# 大公约数指的是数组中所有元素的最大公约数。如果最多更改数组中
# 的一个元素之后，数组的最大公约数为g,那么称g为这个数组的近似
# GCD。一个数组的近似GCD可能有多种取值。
# 具体的，判断g是否为一个子数组的近似GCD如下：
# 1.如果这个子数组的最大公约数就是g,那么说明g是其近似
# GCD.
# 2.在修改这个子数组中的一个元素之后（何以改成想要的任何值），子
# 数组的最大公约数为g,那么说明g是这个子数组的近似GCD。
# 小蓝想知道，数组A有多少个长度大于等于2的子数组满足近似GCD
# 的值为g。
# 输入格式
# 输入的第一行包含两个整数，g,用一个空格分隔，分别表示数组A
# 的长度和g的值。
# 第二行包含n个整数a1,a2,··,an,相邻两个整数之间用一个空格
# 分隔。
# 输出格式
# 输出一行包含一个整数表苏示数组A有多少个长度大于等于2的子数组
# 的近似GCD的值为g。
import math

n,g = map(int,input().split())
nums = [0] + list(map(int,input().split()))
res = 0
left = 1
right = 1
tmp = 0
for right in range(1,n+1):
    t = math.gcd(g,nums[right])
    if t != g:
        left = tmp + 1
        tmp = right
    if right - left + 1 <= 2:
        res += right - left
print(res)
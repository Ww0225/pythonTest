# 请求出在12345678（含）至98765432（含）中，有多少个数中
# 完全不包含2023。
# 完全不包含2023是指无论将这个数的哪些数位移除都不能得到2023
# 例如20322175,33220022都完全不包含2023，而20230415
# 20193213则含有2023（后者取第1,2,6,8个数位）。
goal = ['2','0','2','3']

def fun(n):
    j = 0
    for i in range(len(n)):
        if n[i] == goal[j]:
            j += 1
        if j == 4:
            return False
    return True

count = 0
for i in range(12345678,98765433):
    if fun(str(i)):
        count += 1
print(count)
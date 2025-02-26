import math

n = int(input())
result = 0
result_arr = []

while(True):
    if (math.floor(n/5) == 0):
        break
    n = n // 5
    result_arr.append(n)

for i in result_arr:
    result += i
print(result)
from math import gcd
from datetime import datetime, timedelta

def lcm(a, b):
    return a * b // gcd(a, b)

def lcm_list(nums):
    res = nums[0]
    for num in nums[1:]:
        res = lcm(res, num)
    return res

n = int(input().strip())
cycles = list(map(int, input().split()))
start_date = datetime.strptime(input().strip(), "%Y/%m/%d")
days = lcm_list(cycles)
next_date = start_date + timedelta(days=days)
print(next_date.strftime("%Y/%m/%d"))

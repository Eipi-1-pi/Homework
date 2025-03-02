import math

def is_all_even(num):
    return all((int(digit) % 2 == 0) for digit in str(num))

def find_smallest_even_square(k):
    lower = 10 ** (k - 1)
    upper = 10 ** k - 1
    start = int(math.ceil(math.sqrt(lower)))
    while True:
        square = start * start
        if square > upper:
            return -1
        if is_all_even(square):
            return square
        start += 1


n = int(input().strip())
for _ in range(n):
    k = int(input().strip())
    result = find_smallest_even_square(k)
    print(result)

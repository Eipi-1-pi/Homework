from sys import stdin

def score(mark):
    s = 0
    for i in range(5):
        if all(mark[i][j] for j in range(5)):
            s += 1
    for j in range(5):
        if all(mark[i][j] for i in range(5)):
            s += 1
    if all(mark[i][i] for i in range(5)):
        s += 1
    if all(mark[i][4-i] for i in range(5)):
        s += 1
    return s

board = []
num_to_pos = {}
for i in range(5):
    row = list(map(int, input().split()))
    board.append(row)
    for j, num in enumerate(row):
        num_to_pos[num] = (i, j)

mark = [[False] * 5 for _ in range(5)]
while True:
    x = int(input().strip())
    if x == -1:
        break
    i, j = num_to_pos[x]
    mark[i][j] = True

best_score = -1
best_num = None
for num in range(1, 26):
    i, j = num_to_pos[num]
    if not mark[i][j]:
        mark[i][j] = True
        sc = score(mark)
        if sc > best_score or (sc == best_score and (best_num is None or num < best_num)):
            best_score = sc
            best_num = num
        mark[i][j] = False

print(best_num)


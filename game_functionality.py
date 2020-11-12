
from pprint import pprint
from collections import deque

import random as r

r.seed(12345)
numbers = [0, 2, 4, 8, 16, 32, 64]
tab = [[r.choice(numbers) for j in range(4)] for i in range(4)]
pprint(tab)



def move_elements(row):
    row_length = len(row)
    que = deque()

    for i in row:
        if i == 0:
            continue
        try:
            if que[-1] == i:
                que.pop()
                que.append(i*2)
            else:
                que.append(i)
        except IndexError:  # first check when que is still empty
            que.append(i)

    while len(que) < row_length:
        que.append(0)
    #pprint(f"Modified row: {que}")
    return list(que)


print("Move left")
for row in tab:
    row = move_elements(row)
    print(row)

print("Move right")
for row in tab:
    row = move_elements(row[::-1])[::-1]
    print(row)


from pprint import pprint
from collections import deque

import random as r

r.seed(12345)
numbers = [0, 2, 4, 8, 16, 32, 64]
tab = [[r.choice(numbers) for j in range(4)] for i in range(4)]
pprint(tab)


def switch_elements(row):
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



def move_elements_left(matrix):
    print("Move left")
    new_matrix = deque()
    for row in matrix:
        new_matrix.append(switch_elements(row))
    return list(new_matrix)


def move_elements_right(matrix):
    print("Move right")
    new_matrix = deque()
    for row in matrix:
        new_matrix.append(switch_elements(row[::-1])[::-1])
    return list(new_matrix)

def move_elements_top(matrix):
    pass

def move_elements_down(matrix):
    pass


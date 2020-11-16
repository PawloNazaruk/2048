from pprint import pprint
from collections import deque
import random as r

r.seed(12345)
numbers = [0, 2, 4, 8, 16, 32, 64]
tab = [[r.choice(numbers) for j in range(4)] for i in range(4)]

# TODO: too many elements summing during one move

def move_elements_left(matrix):
    print("Move left: ")
    new_matrix = deque()
    for row in matrix:
        new_matrix.append(switch_elements(row))
    return list(new_matrix)


def move_elements_right(matrix):
    print("Move right: ")
    new_matrix = deque()
    for row in matrix:
        new_matrix.append(switch_elements(row[::-1])[::-1])
    return list(new_matrix)


def move_elements_up(matrix):
    print("Move up: ")
    inverted_matrix = invert_matrix(matrix)
    new_matrix = deque()
    for row in inverted_matrix:
        new_matrix.append(switch_elements(row))
    return list(invert_matrix(new_matrix))


def move_elements_down(matrix):
    print("Move down: ")
    inverted_matrix = invert_matrix(matrix)
    new_matrix = []
    for row in inverted_matrix:
        new_matrix.append(switch_elements(row[::-1])[::-1])
    return list(invert_matrix(new_matrix))


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


def invert_matrix(matrix):
    inverted_matrix = [[] for each_row in matrix]
    for i in matrix:
        for index, j in enumerate(i):
            inverted_matrix[index].append(j)
    #print(f"Inverted matrix:\n{inverted_matrix}")
    return inverted_matrix


def print_mat(matrix):
    text = ""
    for i in matrix:
        text += "["
        for j in i:
            text += str(j) + ","
        text = text[:-1]
        text += "]\n"
    print(text)


print_mat(tab)
print_mat(move_elements_up(tab))


#print(move_elements_up(tab))
#print(move_elements_down(tab))

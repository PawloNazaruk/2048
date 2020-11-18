from collections import deque
import random as r


def start_game(matrix):
    """Fill the given matrix with two random elements."""
    return add_element(add_element(matrix))


def add_element(matrix):
    """Adds random integer from [2,4] to the random coord of the matrix."""
    n = len(matrix)
    while True:
        x = r.randint(0, n-1)
        y = r.randint(0, n-1)
        if matrix[x][y] == 0:
            weights = [.8, .2]
            matrix[x][y] = r.choices([2, 4], weights)[0]
            return matrix


def move_elements_left(matrix):
    """Performs movement of the matrix elements to the left side."""
    new_matrix = deque()
    score = 0
    for row in matrix:
        new_row, score_gained = move_elements(row)
        new_matrix.append(new_row)
        score += score_gained
    return list(new_matrix), score


def move_elements_right(matrix):
    """Performs movement of the matrix elements to the right side."""

    new_matrix = deque()
    score = 0
    for row in matrix:
        new_row, score_gained = move_elements(row[::-1])
        new_matrix.append(new_row[::-1])
        score += score_gained
    return list(new_matrix), score


def move_elements_up(matrix):
    """Performs movement of the matrix elements to the up side."""
    inverted_matrix = invert_matrix(matrix)
    new_matrix = deque()
    score = 0
    for row in inverted_matrix:
        new_row, score_gained = move_elements(row)
        new_matrix.append(new_row)
        score += score_gained
    return list(invert_matrix(new_matrix)), score


def move_elements_down(matrix):
    """Performs movement of the matrix elements to the down side."""
    inverted_matrix = invert_matrix(matrix)
    new_matrix = []
    score = 0
    for row in inverted_matrix:
        new_row, score_gained = move_elements(row[::-1])
        new_matrix.append(new_row[::-1])
        score += score_gained
    return list(invert_matrix(new_matrix)), score


def move_elements(row):
    """Moves elements in the list and sum the score.

    All 0 are dropped from the list, then each remaining element is
    checked with the next if they are the same. If pair like them is
    found they become new element which equals to their sum. At the
    end 0 fills the list to the starting size.

    Returns:
        list(que) - Row after moving it's elements.
        score - Sum of the found pair values.
    """
    row_length = len(row)
    que = deque()
    is_pair = 0
    score = 0
    for val in row:
        if val == 0:
            continue
        try:
            if que[-1] == val and is_pair == 0:
                is_pair = 1  # pair of the same values found, stops searching for new object for current sum
                que.pop()
                que.append(val*2)
                score = val*2
            else:
                if is_pair == 1:
                    is_pair = 0  # value outside of the previous pair, starts searching for the new pair
                que.append(val)
        except IndexError:  # first check when que is still empty
            que.append(val)

    while len(que) < row_length:
        que.append(0)

    return list(que), score


def invert_matrix(matrix):
    """Changes rows with colums."""
    inverted_matrix = [[] for each_row in matrix]
    for i in matrix:
        for index, j in enumerate(i):
            inverted_matrix[index].append(j)
    return inverted_matrix


def game_over(matrix):
    """Ends the game if none from the movements can create new matrix."""
    if matrix != move_elements_left(matrix)[0]:
        return 0
    if matrix != move_elements_right(matrix)[0]:
        return 0
    if matrix != move_elements_up(matrix)[0]:
        return 0
    if matrix != move_elements_down(matrix)[0]:
        return 0
    return "END"
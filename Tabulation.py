import sys


def execute(matrix):
    table = __tabulation__(matrix)
    return "The Result value is: " + str(table[0][0]) + \
        " By taking the following path: " + str(__path_chosen__(table))


def __tabulation__(matrix):
    table = [[0 for _ in range(len(matrix))] for _ in range(len(matrix))]
    table[-1] = matrix[-1]
    for row in reversed(range(0, len(matrix) - 1)):
        for col in range(0, row + 1):
            table[row][col] = matrix[row][col] + min(table[row + 1][col], table[row + 1][col + 1])

    return table


def __path_chosen__(table):
    matrix_index_list = []
    matrix_index = (0, 0)
    matrix_index_list.append(matrix_index)
    for i in range(1, len(table) - 1):
        less_value_item = sys.maxsize
        y = -1
        for j in range(matrix_index_list[len(matrix_index_list) - 1][1],
                       matrix_index_list[len(matrix_index_list) - 1][1] + 2):
            if table[i][j] <= less_value_item:
                less_value_item = table[i][j]
                y = j
        matrix_index_list.append((i, y))

    if table[matrix_index_list[-1][0] + 1][matrix_index_list[-1][1]] < \
            table[matrix_index_list[-1][0] + 1][matrix_index_list[-1][1] + 1]:
        matrix_index_list.append((matrix_index_list[-1][0] + 1, matrix_index_list[-1][1]))
    else:
        matrix_index_list.append((matrix_index_list[-1][0] + 1, matrix_index_list[-1][1] + 1))

    return matrix_index_list

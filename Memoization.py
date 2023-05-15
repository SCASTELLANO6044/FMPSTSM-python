def execute(matrix):
    memoization_dictionary = {}
    matrix_index = (0, 0)
    __memoization__(matrix, memoization_dictionary, matrix_index)
    return "The result value is: " + str(memoization_dictionary[(0, 0)]) + \
        " By taking the following path: " + str(__path_chosen__(matrix, memoization_dictionary))


def __memoization__(matrix, memoization_dictionary, matrix_index):
    if matrix_index in memoization_dictionary:
        return memoization_dictionary[matrix_index]

    if matrix_index[0] == len(matrix) - 2:
        result = matrix[matrix_index[0]][matrix_index[1]] + min(
            matrix[matrix_index[0] + 1][matrix_index[1]], matrix[matrix_index[0] + 1][matrix_index[1] + 1])
        memoization_dictionary[matrix_index] = result
        return result

    else:
        down_element_index = (matrix_index[0] + 1, matrix_index[1])
        righ_down_element_index = (matrix_index[0] + 1, matrix_index[1] + 1)

        down_element = __memoization__(matrix, memoization_dictionary, down_element_index)
        righ_down_element = __memoization__(matrix, memoization_dictionary, righ_down_element_index)

        result = matrix[matrix_index[0]][matrix_index[1]] + min(down_element, righ_down_element)
        memoization_dictionary[matrix_index] = result
        return result


def __path_chosen__(matrix, memoization_dictionary):
    matrix_index_list = []
    matrix_index = (0, 0)
    matrix_index_list.append(matrix_index)

    while matrix_index[0] != len(matrix) - 2:
        down_element_index = (matrix_index[0] + 1, matrix_index[1])
        righ_down_element_index = (matrix_index[0] + 1, matrix_index[1] + 1)
        if memoization_dictionary[down_element_index] < memoization_dictionary[righ_down_element_index]:
            matrix_index_list.append(down_element_index)
            matrix_index = down_element_index
        else:
            matrix_index_list.append(righ_down_element_index)
            matrix_index = righ_down_element_index

    if matrix[matrix_index[0] + 1][matrix_index[1]] < matrix[matrix_index[0] + 1][matrix_index[1] + 1]:
        matrix_index_list.append((matrix_index[0] + 1, matrix_index[1]))
    else:
        matrix_index_list.append((matrix_index[0] + 1, matrix_index[1] + 1))

    return matrix_index_list

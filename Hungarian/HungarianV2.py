import time
import numpy as np



def zero(zM, mark):
    min_row = [99999, -1]
    for row in range(zM.shape[0]):
        if np.sum(zM[row] == True) > 0 and min_row[0] > np.sum(zM[row] == True):
            min_row = [np.sum(zM[row] == True), row]
    z_ind = np.where(zM[min_row[1]] == True)[0][0]
    mark.append((min_row[1], z_ind))
    zM[min_row[1], :] = False
    zM[:, z_ind] = False


def markM(mat):
    current = mat
    zeroM = (current == 0)
    copy_zeroM = zeroM.copy()
    marked_zero = []
    while (True in copy_zeroM):
        zero(copy_zeroM, marked_zero)

    marked_row = []
    marked_column = []
    for i in range(len(marked_zero)):
        marked_row.append(marked_zero[i][0])
        marked_column.append(marked_zero[i][1])
    n_marked_row = list(set(range(current.shape[0])) - set(marked_row))
    marked_columns = []
    check = True
    while check:
        check = False
        for i in range(len(n_marked_row)):
            row_array = zeroM[n_marked_row[i], :]
            for j in range(row_array.shape[0]):
                if row_array[j] == True and j not in marked_columns:
                    marked_columns.append(j)
                    check = True

        for row_num, col_num in marked_zero:
            if row_num not in n_marked_row and col_num in marked_columns:
                n_marked_row.append(row_num)
                check = True
    marked_rows = list(set(range(mat.shape[0])) - set(n_marked_row))

    return (marked_zero, marked_rows, marked_columns)



def adjust_matrix(mat, cover_rows, cover_columns):
    current = mat.copy()
    n_zero_element = []
    for row in range(len(current)):
        if row not in cover_rows:
            for i in range(len(current[row])):
                if i not in cover_columns:
                    n_zero_element.append(current[row][i])
    min_num = min(n_zero_element)
    for row in range(len(current)):
        if row not in cover_rows:
            for i in range(len(current[row])):
                if i not in cover_columns:
                    current[row, i] = current[row, i] - min_num
    for row in range(len(cover_rows)):
        for col in range(len(cover_columns)):
            current[cover_rows[row], cover_columns[col]] = current[cover_rows[row], cover_columns[col]] + min_num
    return current



def hungarian_algorithm(mat):
    dim = mat.shape[0]
    cur_mat = mat
    for row_num in range(mat.shape[0]):
        cur_mat[row_num] = cur_mat[row_num] - np.min(cur_mat[row_num])
    for col_num in range(mat.shape[1]):
        cur_mat[:, col_num] = cur_mat[:, col_num] - np.min(cur_mat[:, col_num])
    zero_count = 0
    while zero_count < dim:
        ans_pos, marked_rows, marked_cols = markM(cur_mat)
        zero_count = len(marked_rows) + len(marked_cols)
        if zero_count < dim:
            cur_mat = adjust_matrix(cur_mat, marked_rows, marked_cols)

    return ans_pos


def calc(mat, pos):
    total = 0
    for i in range(len(pos)):
        total += mat[pos[i][0], pos[i][1]]
    return total

start = time.time()
with open("matrix.txt", "r") as f:
    lines = f.readlines()

matrix = []
for line in lines:
    row = list(map(int, line.strip().split()))
    matrix.append(row)


input_matrix = np.array(matrix)
max_value = np.max(input_matrix)
cost_matrix = max_value - input_matrix
ans_pos = hungarian_algorithm(cost_matrix.copy())
ans = calc(input_matrix, ans_pos)
print(f"The value of the maximum matching >>>> {ans}")
print(f"Program was completed >>>> {time.time()-start} seconds")
import numpy as np
import matplotlib.pyplot as plt


def find_row_continue(two_d_list_temp):
    rule2_row_continue_list_temp = list()
    for i in range(len(two_d_list_temp)):
        for j in range(len(two_d_list_temp[i]) - 1):
            if two_d_list_temp[i][j] == '0':
                continue
            if two_d_list_temp[i][j] == two_d_list_temp[i][j + 1]:  # continue same
                rule2_row_continue_list_temp.append((i, j))
    return rule2_row_continue_list_temp


def set_row_continue_value(rule2_row_continue_list_temp, two_d_list_temp, len_row_temp):
    count_change_time_temp = 0
    for i, j in rule2_row_continue_list_temp:
        if two_d_list_temp[i][j] == 'w':
            if two_d_list_temp[i][j - 1] == '0':
                if j - 1 >= 0:
                    two_d_list_temp[i][j - 1] = 'b'
                    count_change_time_temp += 1
            if j + 2 == len_row_temp:
                continue
            if two_d_list_temp[i][j + 2] == '0':
                two_d_list_temp[i][j + 2] = 'b'
                count_change_time_temp += 1
        if two_d_list_temp[i][j] == 'b':
            if two_d_list_temp[i][j - 1] == '0':
                if j - 1 >= 0:
                    two_d_list_temp[i][j - 1] = 'w'
                    count_change_time_temp += 1
            if j + 2 == len_row_temp:
                continue
            if two_d_list_temp[i][j + 2] == '0':
                two_d_list_temp[i][j + 2] = 'w'
                count_change_time_temp += 1
    return two_d_list_temp, count_change_time_temp


def find_row_jump(two_d_list_temp):
    rule2_row_jump_list_temp = list()
    for i in range(len(two_d_list_temp)):
        for j in range(len(two_d_list_temp[i]) - 2):
            if two_d_list_temp[i][j] == '0':
                continue
            if two_d_list_temp[i][j] == two_d_list_temp[i][j + 2]:  # continue same
                rule2_row_jump_list_temp.append((i, j))
    return rule2_row_jump_list_temp


def set_row_jump_value(rule2_row_jump_list_temp, two_d_list_temp):
    count_change_time_temp = 0
    for i, j in rule2_row_jump_list_temp:
        if two_d_list_temp[i][j] == 'w':
            if two_d_list_temp[i][j + 1] == '0':
                two_d_list_temp[i][j + 1] = 'b'
                count_change_time_temp += 1
        if two_d_list_temp[i][j] == 'b':
            if two_d_list_temp[i][j + 1] == '0':
                two_d_list_temp[i][j + 1] = 'w'
                count_change_time_temp += 1
    return two_d_list_temp, count_change_time_temp


def find_col_continue(two_d_list_temp):
    rule2_col_continue_list_temp = list()
    for i in range(len(two_d_list_temp) - 1):
        for j in range(len(two_d_list_temp[i])):
            if two_d_list_temp[i][j] == '0':
                continue
            if two_d_list_temp[i][j] == two_d_list_temp[i + 1][j]:  # continue same
                rule2_col_continue_list_temp.append((i, j))
    return rule2_col_continue_list_temp


def set_col_continue_value(rule2_col_continue_list_temp, two_d_list_temp, len_col_temp):
    count_change_time_temp = 0
    for i, j in rule2_col_continue_list_temp:
        if two_d_list_temp[i][j] == 'w':
            if two_d_list_temp[i - 1][j] == '0':
                if i - 1 >= 0:
                    two_d_list_temp[i - 1][j] = 'b'
                    count_change_time_temp += 1
            if i + 2 == len_col_temp:
                continue
            if two_d_list_temp[i + 2][j] == '0':
                two_d_list_temp[i + 2][j] = 'b'
                count_change_time_temp += 1
        if two_d_list_temp[i][j] == 'b':
            if two_d_list_temp[i - 1][j] == '0':
                if i - 1 >= 0:
                    two_d_list_temp[i - 1][j] = 'w'
                    count_change_time_temp += 1
            if i + 2 == len_col_temp:
                continue
            if two_d_list_temp[i + 2][j] == '0':
                two_d_list_temp[i + 2][j] = 'w'
                count_change_time_temp += 1
    return two_d_list_temp, count_change_time_temp


def find_col_jump(two_d_list_temp):
    rule2_col_jump_list_temp = list()
    for i in range(len(two_d_list_temp) - 2):
        for j in range(len(two_d_list_temp[i])):
            if two_d_list_temp[i][j] == '0':
                continue
            if two_d_list_temp[i][j] == two_d_list_temp[i + 2][j]:  # continue same
                rule2_col_jump_list_temp.append((i, j))
    return rule2_col_jump_list_temp


def set_col_jump_value(rule2_col_jump_list_temp, two_d_list_temp):
    count_change_time_temp = 0
    for i, j in rule2_col_jump_list_temp:
        if two_d_list_temp[i][j] == 'w':
            if two_d_list_temp[i + 1][j] == '0':
                two_d_list_temp[i + 1][j] = 'b'
                count_change_time_temp += 1
        if two_d_list_temp[i][j] == 'b':
            if two_d_list_temp[i + 1][j] == '0':
                two_d_list_temp[i + 1][j] = 'w'
                count_change_time_temp += 1
    return two_d_list_temp, count_change_time_temp


def full_last_row(two_d_list_temp):
    num = len(two_d_list_temp[0]) / 2
    count_w_list = list()
    count_b_list = list()
    count_0_list = list()
    for i in range(len(two_d_list_temp)):
        count_w_list.append(two_d_list_temp[i].count('w'))
        count_b_list.append(two_d_list_temp[i].count('b'))
        count_0_list.append(two_d_list_temp[i].count('0'))
    for i in range(len(count_0_list)):
        if count_0_list[i] == 1:
            if count_w_list[i] == num - 1:
                two_d_list_temp[i][two_d_list_temp[i].index('0')] = 'w'
            if count_b_list[i] == num - 1:
                two_d_list_temp[i][two_d_list_temp[i].index('0')] = 'b'
    return two_d_list_temp


def full_last_col(two_d_list_temp):
    two_d_list_temp_trans = np.transpose(two_d_list_temp)
    full_last_row(two_d_list_temp_trans.tolist())
    two_d_list_temp = np.transpose(full_last_row(two_d_list_temp_trans.tolist())).tolist()

    return two_d_list_temp


def draw(two_d_list_temp, len_row_temp, len_col_temp):
    ax = plt.subplot(111)
    for i in range(len(two_d_list_temp)):
        for j in range(len(two_d_list_temp[i])):
            if two_d_list_temp[i][j] == 'b':
                print(i, j)
                x1 = np.linspace(j, j + 1, 10)
                ax.fill_between(x1, len_col_temp - 1 - i, len_col_temp - i, facecolor='black')
            if two_d_list_temp[i][j] == 'w':
                print(i, j)
                x1 = np.linspace(j, j + 1, 10)
                ax.fill_between(x1, len_col_temp - 1 - i, len_col_temp - i, facecolor='blue')
    plt.xlim(0, len_row_temp)
    plt.ylim(0, len_col_temp)
    ax.xaxis.grid(True, which='major')  # major,color='black'
    ax.yaxis.grid(True, which='major')  # major,color='black'
    plt.show()


# # built
len_row = 6
len_col = 8
two_d_list = [[0 for i in range(len_row)] for _ in range(len_col)]
# set init
for i in range(len(two_d_list)):
    for j in range(len(two_d_list[i])):
        text = "(i, j)" + "(" + str(i) + ", " + str(j) + "):"
        set_input = input(text)
        two_d_list[i][j] = set_input

print(two_d_list)

# main
run_times = 0
for list_ in two_d_list:
    run_times += list_.count('0')
for a in range(run_times):
    count_change_time = 1
    while count_change_time != 0:
        rule2_row_continue_list = find_row_continue(two_d_list)
        two_d_list, count_change_time = set_row_continue_value(rule2_row_continue_list, two_d_list, len_row)
    count_change_time = 1
    while count_change_time != 0:
        rule2_row_jump_list = find_row_jump(two_d_list)
        two_d_list, count_change_time = set_row_jump_value(rule2_row_jump_list, two_d_list)
    count_change_time = 1
    while count_change_time != 0:
        rule2_col_continue_list = find_col_continue(two_d_list)
        two_d_list, count_change_time = set_col_continue_value(rule2_col_continue_list, two_d_list, len_col)
    count_change_time = 1
    while count_change_time != 0:
        rule2_col_jump_list = find_col_jump(two_d_list)
        two_d_list, count_change_time = set_col_jump_value(rule2_col_jump_list, two_d_list)
    two_d_list = full_last_row(two_d_list)
    two_d_list = full_last_col(two_d_list)

two_d_list = [['0', '0', '0', '0', 'w', '0'],
              ['0', 'w', '0', '0', 'b', '0'],
              ['w', '0', 'b', '0', 'w', '0'],
              ['0', '0', '0', '0', '0', '0'],
              ['0', 'b', 'w', 'b', '0', 'w'],
              ['0', 'w', 'b', 'w', '0', '0'],
              ['0', 'b', 'w', 'b', '0', '0'],
              ['0', '0', '0', 'b', '0', '0']]

draw(two_d_list, len_row, len_col)

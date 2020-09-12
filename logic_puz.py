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
    count_change_time_row_jump_temp = 0
    for i, j in rule2_row_jump_list_temp:
        if two_d_list_temp[i][j] == 'w':
            if two_d_list_temp[i][j + 1] == '0':
                two_d_list_temp[i][j + 1] = 'b'
                count_change_time_row_jump_temp += 1
        if two_d_list_temp[i][j] == 'b':
            if two_d_list_temp[i][j + 1] == '0':
                two_d_list_temp[i][j + 1] = 'w'
                count_change_time_row_jump_temp += 1
    return two_d_list_temp, count_change_time_row_jump_temp


# # built
len_row = 6
len_col = 8
two_d_list = [[0 for i in range(len_row)] for _ in range(len_col)]
# set init
for i in range(len(two_d_list)):
    for j in range(len(two_d_list[i])):
        text = "(i, j)" + "(" + str(i) + ", " + str(j) + "):"
        seinput = input(text)
        two_d_list[i][j] = seinput

print(two_d_list)

# # main
# count_change_time = 1
# while count_change_time != 0:
#     rule2_row_jump_list = find_row_jump(two_d_list)
#     two_d_list, count_change_time = set_row_jump_value(rule2_row_jump_list, two_d_list)
# count_change_time = 1
# while count_change_time != 0:
#     rule2_row_continue_list = find_row_continue(two_d_list)
#     two_d_list, count_change_time = set_row_continue_value(rule2_row_continue_list, two_d_list, len_row)


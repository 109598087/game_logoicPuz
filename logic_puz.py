def find_row_continue(two_d_list_temp):
    rule2_list_temp = list()
    for i in range(len(two_d_list_temp)):
        for j in range(len(two_d_list_temp[i]) - 1):
            if two_d_list_temp[i][j] == '0':
                continue
            if two_d_list_temp[i][j] == two_d_list_temp[i][j + 1]:  # continue same
                rule2_list_temp.append((i, j))
    return rule2_list_temp


def set_row_continue_value(rule2_list_temp, two_d_list_temp, len_row_temp):
    count_change_time_temp = 0
    for t_i, t_j in rule2_list_temp:
        if two_d_list_temp[t_i][t_j] == 'w':
            if two_d_list_temp[t_i][t_j - 1] == '0':
                if t_j - 1 >= 0:
                    two_d_list_temp[t_i][t_j - 1] = 'b'
                    count_change_time_temp += 1
            if t_j + 2 == len_row_temp:
                continue
            if two_d_list_temp[t_i][t_j + 2] == '0':
                two_d_list_temp[t_i][t_j + 2] = 'b'
                count_change_time_temp += 1
        if two_d_list_temp[t_i][t_j] == 'b':
            if two_d_list_temp[t_i][t_j - 1] == '0':
                if t_j - 1 >= 0:
                    two_d_list_temp[t_i][t_j - 1] = 'w'
                    count_change_time_temp += 1
            if t_j + 2 == len_row_temp:
                continue
            if two_d_list_temp[t_i][t_j + 2] == '0':
                two_d_list_temp[t_i][t_j + 2] = 'w'
                count_change_time_temp += 1
    return two_d_list_temp, count_change_time_temp


# # built
len_row = 6
len_col = 8
# two_d_list = [[0 for i in range(len_row)] for _ in range(len_col)]
# # set init
# for i in range(len(two_d_list)):
#     for j in range(len(two_d_list[i])):
#         text = "(i, j)" + "(" + str(i) + ", " + str(j) + "):"
#         set_input = input(text)
#         two_d_list[i][j] = set_input
two_d_list = [['0', 'w', '0', '0', '0', 'b'],
              ['0', '0', 'w', 'w', 'b', '0'],
              ['0', 'w', 'b', 'w', 'w', '0'],
              ['w', 'b', 'w', '0', '0', '0'],
              ['b', 'w', '0', 'b', '0', '0'],
              ['b', '0', '0', 'w', '0', '0'],
              ['0', 'b', 'b', '0', 'w', 'b'],
              ['w', 'b', '0', 'b', '0', 'w']]

# rule2
count_change_time = 1
while count_change_time != 0:
    rule2_list = find_row_continue(two_d_list)
    two_d_list, count_change_time = set_row_continue_value(rule2_list, two_d_list, len_row)

two_d_list = [['0', 'w', '0', '0', '0', 'b'],
              ['0', 'b', 'w', 'w', 'b', '0'],
              ['0', 'w', 'b', 'w', 'w', 'b'],
              ['w', 'b', 'w', '0', '0', '0'],
              ['b', 'w', '0', 'b', '0', '0'],
              ['b', '0', '0', 'w', '0', '0'],
              ['w', 'b', 'b', 'w', 'w', 'b'],
              ['w', 'b', '0', 'b', '0', 'w']]

#!/usr/bin/python3
def weight_average(my_list=[]):
    average, num1, num2 = 0, 0, 0
    if not my_list:
        return 0
    for i in range(len(my_list)):
        for j in range(len(my_list[i])):
            if j == 0:
                num1 += my_list[i][j] * my_list[i][j + 1]
                num2 += my_list[i][j + 1]
    average = num1 / num2
    return average

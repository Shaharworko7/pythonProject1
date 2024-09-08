# matrix = [
#     [1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 10],
#     [11, 12, 13, 14, 15],
#     [16, 17, 18, 19, 20],
#     [21, 22, 23, 24, 25]
# ]
# for i in range(len(matrix)):
#     print(matrix[i])


# matrix = [
#     [1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 10],
#     [11, 12, 13, 14, 15],
#     [16, 17, 18, 19, 20],
#     [21, 22, 23, 24, 25]
# ]
# for i in range(len(matrix)):
#     sum1 = sum(matrix[i])
#     sum1 += sum1
# print(sum1)

# matrix = [
#     [1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 10],
#     [11, 12, 13, 14, 15],
#     [16, 17, 18, 19, 20],
#     [21, 22, 23, 24, 25]
# ]
# num = 0
# for i in range(len(matrix)):
#     cell = matrix[i][i]
#     num += cell
# print(num)

import random

# from random import *
# matr = []
# matr1 = []
# for i in range(3):
#     matr1 = [randrange(1, 100) for j in range(3)]
#     matr.append(matr1)
# print(matr)
# matr2 = []
# matr3 = [[], [], []]
# for i in range(3):
#     for j in range(3):
#         cell = matr[j][i]
#         matr3 = [cell for j in range(1)]
#         matr2.append(cell)
#         print(cell)
# print(matr2)

# matrix = [
#     [1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 10],
#     [11, 12, 13, 14, 15],
#     [16, 17, 18, 19, 20],
#     [21, 22, 23, 24, 25]
# ]
# for i in range(len(matrix)):
#     if i % 2 != 0:
#         row = matrix[i]
#         row.reverse()
# print(matrix)

# guests = {'vip': ['ofir', 'bar', 'neta'],
#           'fam': ['aviram', 'ohad', ],
#           'fri': ['moti', 'liron', 'roni']}
# for i in guests:
#     print(guests[i])
# bale = input("who cant come?")
# come = input("who will come instead?")
# guests.pop('vip')
# if bale == 'ofir':
#     guests['vip'] = ['bar', 'neta', come]
# elif bale == 'bar':
#     guests['vip'] = ['ofir', 'neta', come]
# elif bale == 'neta':
#     guests['vip'] = ['ofir', 'bar', come]

# matrix = []
# matrix2 = []
# len_matrix = int(input("enter the length of the matrix "))
# for i in range(int(len_matrix)):
#     matrix.append([])
#     for j in range(int(len_matrix)):
#         matrix[i].append((len_matrix * i + j + 1))
#
# for i in range(int(len_matrix)):
#     matrix2.append([])
#     for j in range(int(len_matrix)):
#         matrix2[i].append((len_matrix * i + j + 1))
#
# for i in range(len_matrix):
#     print(matrix[i])
#
# for row in range(len_matrix):
#     for col in range(len_matrix):
#         matrix[col][len_matrix - row - 1] = matrix2[row][col]
# for i in range(len_matrix):
#     print(matrix[i])

# len_matrix = int(input("enter matrix size"))
# for row in range(len_matrix):
#     matrix = []
#     for col in range(len_matrix):
#         num = row - col
#         if num < 0:
#             num =0
#             matrix.append(num)
#         else:
#             matrix.append(num)
#     print(matrix)

# 9
# WORKING_SCREEN = "work"
# FAULTY_SCREEN = "problem"
# tv = [
#     [WORKING_SCREEN, WORKING_SCREEN, WORKING_SCREEN, WORKING_SCREEN, WORKING_SCREEN],
#     [WORKING_SCREEN, WORKING_SCREEN, FAULTY_SCREEN, WORKING_SCREEN, WORKING_SCREEN],
#     [WORKING_SCREEN, FAULTY_SCREEN, FAULTY_SCREEN, WORKING_SCREEN, WORKING_SCREEN],
#     [WORKING_SCREEN, WORKING_SCREEN, WORKING_SCREEN, FAULTY_SCREEN, WORKING_SCREEN],
#     [WORKING_SCREEN, WORKING_SCREEN, WORKING_SCREEN, WORKING_SCREEN, FAULTY_SCREEN]
# ]
# for row in range(len(tv)):
#     for col in range(len(tv)):
#         if tv[row][col] == FAULTY_SCREEN:
#             print(FAULTY_SCREEN ,[row,col])


# # 10 לא רץ
# restaurant_layout = [
#     [4, 2, 6, 3],
#     [8, 3, 2, 5],
#     [5, 7, 3, 6],
#     [9, 4, 2, 8]
# ]
# restaurant_layout2 = []
# reservations1 = []
# reservations = [
#     ["Group A", 3],
#     ["Group B", 6],
#     ["Group C", 2],
#     ["Group D", 7],
#     ["Group E", 5],
#     ["Group F", 4],
#     ["Group G", 8],
#     ["Group H", 3],
#     ["Group I", 9],
#     ["Group J", 6]
# ]
# num = 0
# for i in range(len(reservations)):
#      reservations1.append(reservations[i][1])
# for j in range(len(restaurant_layout)):
#     restaurant_layout2.append(restaurant_layout[j][1])
# num = 0
# for i in reservations1:
#     for j in restaurant_layout:
#         if j[num] >= reservations1[num]:
#             print(j[num], reservations[num])
#         num += 1

# 11
# position_row = int(input("enter the quin row"))
# position_col = int(input("enter the quin column"))
# str1 = 'x'
# chess_board = [[0, 0, 0, 0, 0, 0, 0, 0],
#                [0, 0, 0, 0, 0, 0, 0, 0],
#                [0, 0, 0, 0, 0, 0, 0, 0],
#                [0, 0, 0, 0, 0, 0, 0, 0],
#                [0, 0, 0, 0, 0, 0, 0, 0],
#                [0, 0, 0, 0, 0, 0, 0, 0],
#                [0, 0, 0, 0, 0, 0, 0, 0],
#                [0, 0, 0, 0, 0, 0, 0, 0],]

# chess_board[position_row][position_col] = str1
# for i in chess_board:
#     print(i)
# Создайте программу для игры в ""Крестики-нолики"".

import os 
os.system('cls')

pole = [1, 2, 3,
        4, 5, 6,
        7, 8, 9]

win_lines = [[0, 1, 2], [3, 4, 5], [6, 7, 8], 
             [0, 3, 6], [1, 4, 7], [2, 5, 8],
             [0, 4, 8], [2, 4, 6]]

def print_pole():
    # os.system('cls')
    for i in range(9):
        print(f'{pole[i]}\t', end="")
        if not (i+1) % 3:
            print('\n')

def step_(step, symbol):
    ind = pole.index(step)
    pole[ind] = symbol


def game_status():
    win = ""
 
    for elem in win_lines:
        if pole[elem[0]] == "X" and pole[elem[1]] == "X" and pole[elem[2]] == "X":
            win = "X"
        if pole[elem[0]] == "O" and pole[elem[1]] == "O" and pole[elem[2]] == "O":
            win = "O"   
    return win

game_over = False
player1 = True
 
while game_over == False:
    
#  печать игрового поля
    print_pole()
 
    if player1 == True:
        symbol = "X"
        step = int(input("Игрок №1, выберети позицию: "))
    else:
        symbol = "O"
        step = int(input("Игрок №2, выберети позицию: "))
 
    step_(step,symbol) # делаем ход в указанную ячейку
    win = game_status() # определим победителя
    if win != "":
        game_over = True
    else:
        game_over = False
 
    player1 = not(player1)        
 
# Игра окончена. Покажем карту. Объявим победителя.        
print_pole()
print("Победил", win) 
print_pole()

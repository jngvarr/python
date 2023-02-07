# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайт
# е как наделить бота ""интеллектом""

import random
import os
os.system("cls")
global candies

def take_candies(step):
    while 0 >= step or step > 28:
        step = int(
            input(f'Ты можешь взять от 1 до 28 конфет. И никак иначе!!! Сколько? -> '))
    cand = candies-step
  

    
def bot():
    step = random.randint(1, 28)
    while step > candies:
        step = random.randint(1, 28)
    return step


def smart_bot():
    if candies <= 28:
        step = candies
    else:
        step = candies % (28+1)
    if step == 0:
        print("Мегамозг: ""Попробую притвориться ветошью. Вдруг не заметят и поверят.""")
        step = bot(candies)
    return step


def main():
    step = 0
    player1 = True
    candies = 78
    game_over = False
    modes = {1: "Human", 2: "Железка", 3: "СверхРазум"}
    mode = menu(modes)
    print(
        f"На столе {candies} конфет. Ваш противник: {modes[mode]}. Погнали!!")
    while game_over == False:

        if player1:
            step = int(
                input("Игрок №1, твой ход. Сколько конфет ты возьмешь?: "))
        else:
            if mode == 1:
                step = int(
                    input("Игрок №2, твой ход. Сколько конфет ты возьмешь?: "))
            elif mode == 2:
                step = bot(candies)
                print(f"Железка берет {step} конфет(ы).")
            else:
                step = smart_bot(candies)
                print(f"Мегамозг берет {step} конфет(ы).")

        candies = take_candies(step, candies)  
        print(f'Осталось {candies} конфет(ы).')

        if not candies:  
            game_over = True
            if player1:  
                winner = "Игрок №1"
            else:
                if mode == 1:
                    winner = "Игрок №2"
                else:
                    winner = modes[mode]
        else:
            game_over = False
            player1 = not (player1)

    print(f"Победил {winner}. Поздравляю!!!")


if __name__ == '__main__':
    main()

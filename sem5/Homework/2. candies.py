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


def take_candies(step, candies):
    while 0 >= step or step > 28:
        step = int(
            input(f'Ты можешь взять от 1 до 28 конфет. И никак иначе!!! Сколько? -> '))
    cand = candies-step
    while cand < 0:
        step = int(input(f'Жадина!! Попробуй еще раз! Сколько? -> '))
        cand = candies-step
    return cand


def menu(modes):
    game_mode = int(input(f'C кем будешь играть? Выбери режим: \n'+''.join(str(k) +
    '. Human vs ' + str(v) + ' - жми ' + str(k) + '\n' for k, v in modes.items())+" -> "))
    while game_mode > 3 or game_mode < 0:
        game_mode = int(input("Ты точно туда пришел? "))
    return game_mode


def bot(candies):
    step = random.randint(1, 28)
    while step > candies:
        step = random.randint(1, 28)
    return step


def smart_bot(candies):
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

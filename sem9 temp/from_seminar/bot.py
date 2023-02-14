from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import candybot_programs

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global modes
    await update.message.reply_text(f'Условие задачи: На столе лежит 2021 конфета.\
    Играют два игрока делая ход друг после друга. За один ход можно забрать не более чем 28 конфет.\
    Все конфеты оппонента достаются сделавшему последний ход.')
    await update.message.reply_text(f'C кем будешь играть? Выбери режим: \n'+''.join(str(k) +
    '. Human vs ' + str(v) + ' - жми ' "/"+ str(k) + '\n' for k, v in modes.items())+" -> ")

async def game_mode (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global mode
    mode = int(update.message.text)
    global candies
    await update.message.reply_text(f"На столе {candies} конфет. Ваш противник: {modes[mode]}. Погнали!!")
    await update.message.reply_text(f"Сколько конфет ты возьмешь?")



mode = 0
# app.add_handler(CommandHandler("hello", hello))
# app.add_handler(CommandHandler("hello", hello))
app = ApplicationBuilder().token("6168262957:AAE4E5CdM9R8OaQaC7c0Tfa7U892uGb92is").build()
modes = {1: "Human", 2: "Железка", 3: "СверхРазум"}
app.add_handler(MessageHandler(filters.TEXT, hello))
app.add_handler(MessageHandler(filters.TEXT, game_mode))



if mode == 1: app.add_handler(MessageHandler(filters.TEXT, candybot_programs.take_candies))
elif mode == 2: app.add_handler(MessageHandler(filters.TEXT, candybot_programs.bot))
else: app.add_handler(MessageHandler(filters.TEXT, candybot_programs.smart_bot))
    # while game_over == False:
# app.add_handler(MessageHandler(filters.TEXT, hello))

print("start")
app.run_polling()
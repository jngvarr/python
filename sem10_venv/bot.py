import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
import input_
import emoji
import spy as log

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO 
)
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log.log(update, context)
    await update.message.reply_text('Для того, чтобы начать, введите /start')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log.log(update, context)
    await update.message.reply_text(emoji.emojize('Калькулятор рациональных и комплексных чисел.\n\
Введите через пробел два числа и оператор.\n\
Например так: 5_6_*. Нижнее подчеркивание ставить не надо:full_moon_face:'), reply_markup=markup)

async def calculate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log.log(update, context)
    num1, num2, operate = (update.message.text).split()
    data = input_.input_bot_data(num1, num2, operate)
    await update.message.reply_text( text=(emoji.emojize(f'Результат вычисления: {num1} {operate} {num2} = {data}:fire:' )))

# if __name__ == '__main__':
app = ApplicationBuilder().token('6168262957:AAE4E5CdM9R8OaQaC7c0Tfa7U892uGb92is').build()

kb = [ ["/help"],["/start"]]
markup = ReplyKeyboardMarkup(kb, one_time_keyboard=True)

app.add_handler(CommandHandler('start', start))
app.add_handler(CommandHandler('help', help))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, calculate))

print("bot started")
app.run_polling()
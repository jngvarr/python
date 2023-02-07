import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
import input_

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO 
)

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Для того, чтобы начать, введите /start')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Калькулятор, введите через пробел два числа и оператор. Например так: 5_6_*')

async def calculate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data=(update.message.text).split()
    num1, num2, operate = data
    print(num1, num2, operate)
    print(data)
    data = input_.input_bot_data(data)
    await update.message.reply_text( text=(f'Результат вычисления: {num1} {operate} {num2} = {data}' ))

if __name__ == '__main__':
    app = ApplicationBuilder().token('6168262957:AAE4E5CdM9R8OaQaC7c0Tfa7U892uGb92is').build()
    
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('help', help))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, calculate))
    
    
    
    # app.add_handler(start_handler)
    print("bot started")

    app.run_polling()
import logging
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters, Updater, CallbackQueryHandler
import input_
import emoji
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update, InlineKeyboardButton, InlineKeyboardMarkup
import spy as log

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO 
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a message with three inline buttons attached."""
    keyboard = [
        [
            InlineKeyboardButton("help", callback_data='help'),
            InlineKeyboardButton("prompt", callback_data='prompt'),
        ],
        [InlineKeyboardButton("close", callback_data="3")],
    ]
    print(keyboard[0])
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Please choose:", reply_markup=reply_markup)
    

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    # print(update.message.)
    query = update.callback_query
    # print(query)
    await query.answer()
    await query.answer()
    print(query.data)
    if query.data == 'help': help
    elif query.data == 'prompt': prompt
    # await query.edit_message_text(text=f"/{query.data}")


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log.log(update, context)
    # query = update.callback_query
    # print(query)
    # print(query)
        # await query.edit_message_text(text=f"Selected option: {query.data}")
    await update.message.reply_text('Для того, чтобы начать, введите /start')

async def prompt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log.log(update, context)
    await update.message.reply_text(emoji.emojize('Калькулятор рациональных и комплексных чисел.\n\
Введите через пробел два числа и оператор.\n\
Например так: 5_6_*. Нижнее подчеркивание ставить не надо:full_moon_face:'))

async def calculate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log.log(update, context)
    num1, num2, operate = (update.message.text).split()
    data = input_.input_bot_data(num1, num2, operate)
    await update.message.reply_text( text=(emoji.emojize(f'Результат вычисления: {num1} {operate} {num2} = {data}:fire:' )))


def main() -> None:
    app = ApplicationBuilder().token('6168262957:AAE4E5CdM9R8OaQaC7c0Tfa7U892uGb92is').build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CallbackQueryHandler(button))
    # app.add_handler(CallbackQueryHandler(help, pattern="^" + str(help) + "$"))
    # app.add_handler(CallbackQueryHandler(prompt, pattern="^" + str(prompt) + "$"))
    app.add_handler(CommandHandler('prompt', prompt))
    app.add_handler(CommandHandler('help', help))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, calculate))
    print("bot started")
    app.run_polling()

if __name__ == "__main__":
    main()
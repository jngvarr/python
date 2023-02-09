from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters
)
import spy
import input_
import logging
import emoji

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Stages
START_ROUTES = range(1)
# Callback data
END, BEGIN, HELP = range(3)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    logger.info("User %s started the conversation.", user.first_name)
   
    keyboard = [
        [
            InlineKeyboardButton("Закончить работу", callback_data=str(END)),
            InlineKeyboardButton("Начать вычисления", callback_data=str(BEGIN)),
        ],
        [InlineKeyboardButton("Помоги мне", callback_data=str(HELP))],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Выберите, что хотите сделать: ", reply_markup=reply_markup)
    return START_ROUTES


async def prompt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    spy.log(update, context)
    await query.edit_message_text(emoji.emojize('Калькулятор рациональных и комплексных чисел.\n\
Введите через пробел два числа и оператор.\n\
Например так: 5_6_*. Нижнее подчеркивание ставить не надо:full_moon_face:'))


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None: 
    spy.log(update, context)
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text=f'Для того, чтобы начать, введите /start')


async def calculate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    spy.log(update, context)
    num1, num2, operate = (update.message.text).split()
    data = input_.input_bot_data(num1, num2, operate)
    await update.message.reply_text( text=(emoji.emojize(f'Результат вычисления: {num1} {operate} {num2} = {data}:fire:' )))


async def end(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    spy.log(update, context)
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text="Спасибо, что использовали нашу программу")
    return ConversationHandler.END


def main() -> None:
    application = Application.builder().token("6168262957:AAE4E5CdM9R8OaQaC7c0Tfa7U892uGb92is").build()
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            START_ROUTES: [
                CallbackQueryHandler(end, pattern="^" + str(END) + "$"),
                CallbackQueryHandler(prompt, pattern="^" + str(BEGIN) + "$"),
                CallbackQueryHandler(help, pattern="^" + str(HELP) + "$"),
            ],
        },
        fallbacks=[CommandHandler("start", start)],
    )

    application.add_handler(conv_handler)
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, calculate))
    application.run_polling()

if __name__ == "__main__":
    main()

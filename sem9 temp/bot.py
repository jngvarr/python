import logging
import emoji
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


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Stages
START_ROUTES = range(1)
# Callback data
ADD, LIST, END, HELP = range(4)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    logger.info("User %s started the conversation.", user.first_name)
   
    keyboard = [
        [
            InlineKeyboardButton("Добавить новый контакт", callback_data=str(ADD)),
            InlineKeyboardButton("Вывести на экран книгу контактов", callback_data=str(LIST)),InlineKeyboardButton("Помоги мне", callback_data=str(HELP))
        ],
        [InlineKeyboardButton("Помоги мне", callback_data=str(END))],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Выберите, что хотите сделать: ", reply_markup=reply_markup)
    return START_ROUTES


async def prompt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.edit_message_text("")


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None: 
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text=f'Для того, чтобы начать, введите /start')


async def calculate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    num1, num2, operate = (update.message.text).split()
    data = input_.input_bot_data(num1, num2, operate)
    await update.message.reply_text( text=(emoji.emojize(f'Результат вычисления: {num1} {operate} {num2} = {data}:fire:' )))


async def end(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
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
                CallbackQueryHandler(add, pattern="^" + str(ADD) + "$"),
                CallbackQueryHandler(prompt, pattern="^" + str(LIST) + "$"),
                CallbackQueryHandler(help, pattern="^" + str(HELP) + "$"),
                CallbackQueryHandler(end, pattern="^" + str(END) + "$"),
            ],
        },
        fallbacks=[CommandHandler("start", start)],
    )

    application.add_handler(conv_handler)
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, calculate))
    application.run_polling()

if __name__ == "__main__":
    main()

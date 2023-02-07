from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token("6168262957:AAE4E5CdM9R8OaQaC7c0Tfa7U892uGb92is").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(MessageHandler(filters.TEXT, start))


print("start")
app.run_polling()
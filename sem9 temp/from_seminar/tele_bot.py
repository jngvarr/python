from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hola {update.effective_user.first_name}')
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(chat_id=update.effective_chat.id, text = "it's a first bot python")

app = ApplicationBuilder().token("6168262957:AAE4E5CdM9R8OaQaC7c0Tfa7U892uGb92is").build()

app.add_handler(CommandHandler("hola", hello))
app.add_handler(CommandHandler("answer", start))

print("hello")
app.run_polling()
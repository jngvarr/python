choice = 1

async def your_choiсe(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text.split()[1]
    if text == '2':
        global choice
        choice = 2
        await update.message.reply_text('Вы выбрали игрок против компьютера')
    else:
        await update.message.reply_text('Вы выбрали игрок против игрока')

app.add_handler(CommandHandler("choice", your_choiсe))

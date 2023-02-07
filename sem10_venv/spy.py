from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import os

def log(update: Update, context: CallbackContext):
    file = open(os.path.dirname(os.path.abspath(__file__))+'db.csv', 'a')
    file.write(f'{update.effective_user.first_name},{update.effective_user.id}, {update.message.text}\n' )
    file.close()     
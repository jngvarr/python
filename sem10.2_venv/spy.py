from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import os, datetime

def log(update: Update, context: CallbackContext):
    file = open(os.path.dirname(os.path.abspath(__file__))+'\db.csv', 'a')
    file.write(f'{datetime.datetime.now()}, username-{update.effective_user.username}, id-{update.effective_user.id} \n' )
    file.close()
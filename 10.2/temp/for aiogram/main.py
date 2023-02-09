from aiogram import executor
import tictactoe
from tictactoe import dp

async def startup():
    print('bot run')

executor.start_polling(dp, skip_updates=True, on_startup='startup')
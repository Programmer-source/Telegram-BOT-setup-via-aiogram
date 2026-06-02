import asyncio
import logging

from aiogram import Bot,Dispatcher,types
from aiogram.filters import Command

myToken = "YOUR TOKEN HERE"

bot = Bot(myToken)
dp = Dispatcher()

@dp.message(Command("start")) #hook to command /start
async def start_command(message: types.Message):
    await message.answer("Hello world! I am ready to obey your commands!")

async def main(): #launch bot
    logging.basicConfig(level=logging.INFO) #Setting up the basics of the bot (console to monitor the bot)
    await dp.start_polling(bot) #Informing dispatch to start running the bot
asyncio.run(main())

from aiogram import Bot
from aiogram.types import BotCommand


async def set_commands_menu(bot: Bot):
    menu_commands = [
        BotCommand(command='add_video', description='Добавить видео'),
        BotCommand(command='list_video', description='Добавленные видео'),
        BotCommand(command='help', description='Справка по командам'),
        BotCommand(command='cancel', description='Отмена')
    ]
    await bot.set_my_commands(menu_commands)

import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command, CommandStart, Text

from config_data.config import Config, load_config
from database.db_settings import async_session
from keyboards.set_menu import set_commands_menu
import handlers.fsm_handlers
from handlers.user_handlers import process_start_command, process_help_command, process_video_list_command, \
    send_echo, not_correct_url, process_edit_video_list, process_cancel_redact_press, process_delete_video_press
from middlewares.db_authorization_chek import IsAuthorizedDB
from states.states import FSMFillInfo
from utils.callback import video_callback
from utils.callbackdata import VideoInfo
from filters.youtube_filter import IsYouTubeUrl
from filters.video_list_del import IsDeleteVideo


logger = logging.getLogger(__name__)


async def start_bot(bot: Bot):
    await bot.send_message(360012591, text='Бот запущен!')


async def stop_bot(bot: Bot):
    await bot.send_message(360012591, text='Бот остановлен!')


async def main():
    logging.basicConfig(level=logging.INFO,
                        format=u'%(filename)s:%(lineno)d #%(levelname)-8s'
                               u'[%(asctime)s] - %(name)s - %(message)s')

    logger.info('Starting bot')
    storage: MemoryStorage = MemoryStorage()
    config: Config = load_config()

    bot: Bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp: Dispatcher = Dispatcher(storage=storage)

    await set_commands_menu(bot)

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    #  middleware на проверку авторизации пользователя
    dp.message.middleware(IsAuthorizedDB())
    # команда старт, регистрация пользователя
    dp.message.register(process_start_command, CommandStart())
    # вызов всех добавленных видео
    dp.message.register(process_video_list_command, Command(commands='list_video'))
    # редактируем list_video
    dp.callback_query.register(process_edit_video_list, Text(text='edit_video_list'))
    # удаляем видео из list_video
    dp.callback_query.register(process_delete_video_press, IsDeleteVideo())
    # прерываем редактор list_video
    dp.callback_query.register(process_cancel_redact_press, Text(text='cancel_redact'))
    # создаем callback после команды list_video
    dp.callback_query.register(video_callback, VideoInfo.filter())
    # команда help
    dp.message.register(process_help_command, Command(commands='help'))
    # прерываем процесс добавления имени
    dp.message.register(handlers.process_cancel_command, Command(commands='cancel'))
    # начинаем процесс добавления имени
    dp.message.register(handlers.process_get_video_command, Command(commands='add_video'))
    # сохраняем название видео и урл в БД
    dp.message.register(handlers.process_video_name_save, FSMFillInfo.fill_video_name)
    # Проверяем добавлен ли корректный url
    dp.message.register(handlers.process_get_url, FSMFillInfo.fill_url, IsYouTubeUrl())
    # ответ если неверно указан url
    dp.message.register(not_correct_url, FSMFillInfo.fill_url)
    # ответ на любое сообщение от авторизованного юзера
    dp.message.register(send_echo)

    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot, session_maker=async_session)

    finally:
        await bot.close()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error('Bot stopped!')

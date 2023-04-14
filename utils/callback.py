from aiogram.types import CallbackQuery

from .callbackdata import VideoInfo
from services.services import get_data_from_youtube
from lexicon.lexicon_ru import LEXICON_RU


async def video_callback(callback: CallbackQuery, callback_data: VideoInfo):
    await callback.message.answer(LEXICON_RU['loading_info'])
    video_info = get_data_from_youtube(callback_data.url)
    answer = f"Статистика на данный момент: \r\n\n" \
             f"🙉 Просмотры: {video_info['views']} \n" \
             f"🙊 Дата публикации: {video_info['publication_date']} \n" \
             f"🙈 Лайки: {video_info['likes']}👍\n"

    await callback.message.answer(answer)
    await callback.answer()

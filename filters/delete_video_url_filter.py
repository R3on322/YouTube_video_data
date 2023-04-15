from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery
from lexicon.lexicon_ru import LEXICON_RU


class DeleteVideoUrl(BaseFilter):
    async def __call__(self, callback: CallbackQuery):
        return isinstance(callback.data, str) and LEXICON_RU["del"] in callback.data

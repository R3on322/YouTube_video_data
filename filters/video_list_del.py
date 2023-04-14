from aiogram.filters import BaseFilter
from aiogram.types import Message, CallbackQuery


class IsDeleteVideo(BaseFilter):
    async def __call__(self, callback: CallbackQuery):
        return isinstance(callback.data, str) and 'delete' in callback.data

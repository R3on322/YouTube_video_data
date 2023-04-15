from aiogram.filters.callback_data import CallbackData


class VideoInfo(CallbackData, sep=' ', prefix=''):
    id: int
    url: str


from aiogram.filters import BaseFilter
from aiogram.types import Message

import re


class IsYouTubeUrl(BaseFilter):

    async def __call__(self, message: Message) -> bool:
        if re.match(r'^((https://){0,8}[w]{0,3}[\.]{0,1}youtu[\.]{0,1}be(.com/watch){0,10}).*$', message.text):
            print('Url correct')
            return True
        else:
            print('Url NOT correct')
            return False


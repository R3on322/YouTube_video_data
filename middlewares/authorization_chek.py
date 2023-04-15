from typing import Callable, Awaitable, Dict, Any
from aiogram import BaseMiddleware
from aiogram.types import Message
from database.db_crud import create_user, is_authorized
from lexicon.lexicon_ru import LEXICON_RU


class IsAuthorizedDB(BaseMiddleware):

    async def __call__(self,
                       handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
                       event: Message,
                       data: Dict[str, Any],
                       ) -> Any:
        if not await is_authorized(message=event):
            if event.text == '/start':
                await create_user(message=event)
                return await handler(event, data)
            else:
                await event.answer(text=LEXICON_RU['not_authorized'])
        else:
            return await handler(event, data)


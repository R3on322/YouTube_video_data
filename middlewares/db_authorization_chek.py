from typing import Callable, Awaitable, Dict, Any

from lexicon.lexicon_ru import LEXICON_RU

from aiogram import BaseMiddleware
from aiogram.types import Message
from database.db_models import User
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy import select


async def is_authorized(message, async_session) -> bool:
    async with async_session() as session:
        async with session.begin():
            result = await session.execute(select(User).where(User.user_id == message.from_user.id))
            user = result.one_or_none()
            if user is None:
                return False
            else:
                return True


async def create_user(message, async_session):
    new_user = User(user_id=message.from_user.id,
                    user_name=message.from_user.first_name)
    async with async_session() as session:
        async with session.begin():
            session.add(new_user)
            print('Пользователь добавлен')


class IsAuthorizedDB(BaseMiddleware):

    async def __call__(self,
                       handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
                       event: Message,
                       data: Dict[str, Any],
                       ) -> Any:

        async_session: async_sessionmaker = data['session_maker']

        if not await is_authorized(message=event, async_session=async_session):
            if event.text == '/start':
                await create_user(event, async_session)
                return await handler(event, data)
            else:
                await event.answer(text=LEXICON_RU['not_authorized'])
        else:
            return await handler(event, data)


from .db_models import UserVideoInfo, User
from .db_settings import async_session
from sqlalchemy import select


async def create_user(message):
    new_user = User(user_id=message.from_user.id,
                    user_name=message.from_user.first_name)
    async with async_session() as session:
        async with session.begin():
            session.add(new_user)
            print('Пользователь добавлен')


async def get_list_video(user_id) -> object:
    async with async_session() as session:
        async with session.begin():
            video_url = await session.execute(
                select(UserVideoInfo.video_name, UserVideoInfo.video_url).where(UserVideoInfo.user_id == user_id)
            )
            video_url = video_url.all()
            return video_url


async def add_video_url(user_id, video_name, url) -> None:
    video_data = UserVideoInfo(
        user_id=user_id,
        video_name=video_name,
        video_url=url
    )
    async with async_session() as session:
        async with session.begin():
            session.add(video_data)


async def is_authorized(message) -> bool:
    async with async_session() as session:
        async with session.begin():
            result = await session.execute(select(User).where(User.user_id == message.from_user.id))
            user = result.one_or_none()
            if user is None:
                return False
            else:
                return True


async def delete_video():
    pass

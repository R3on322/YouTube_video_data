from .db_models import UserVideoInfo
from .db_settings import async_session
from sqlalchemy import select

user_dict_template: dict = {}

users_db: dict = {
    360012591:
        {'Dota 2 WTF Moments 465 - YouTube': 'https://www.youtube.com/watch?v=uEFBOaIdBqg',
         'Ответила на ваши вопросы из инсты 🥰 - YouTube': 'https://www.youtube.com/watch?v=EITuxtgWNyk'
         }
}


async def get_all_url(user_id):
    async with async_session() as session:
        async with session.begin():
            video_url = await session.execute(
                select(UserVideoInfo.video_name, UserVideoInfo.video_url).where(UserVideoInfo.user_id == user_id)
            )
            video_url = video_url.all()
            return video_url


async def add_video_url(user_id, video_name, url):
    video_data = UserVideoInfo(
        user_id=user_id,
        video_name=video_name,
        video_url=url
    )
    async with async_session() as session:
        async with session.begin():
            session.add(video_data)



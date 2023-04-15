from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from lexicon.lexicon_ru import LEXICON_RU
from states.states import FSMFillInfo
from database.db_crud import add_video_url
from services.services import get_data_from_youtube


async def process_get_video_command(message: Message, state: FSMContext):
    await message.answer(text=f"{message.from_user.first_name}, {LEXICON_RU[message.text]}")
    await state.set_state(FSMFillInfo.fill_url)
    print('Добавляем видео')


async def process_get_url(message: Message, state: FSMContext):
    await state.update_data(url=message.text)
    await state.set_state(FSMFillInfo.fill_video_name)
    print('Сохранили ссылку')
    await message.answer(text=LEXICON_RU['name_for_video'])


async def process_video_name_save(message: Message, state: FSMContext):
    video_data = await state.get_data()
    await message.answer(text=LEXICON_RU['loading_info'])
    dict_video_info = get_data_from_youtube(video_data['url'])
    await state.update_data(video_name=dict_video_info['video_name'])
    if message.text != '/skip':
        await state.update_data(video_name=message.text)
        print('Сохранили название для видео')
        await message.answer(text=f'Сохранил названия для видео - "{message.text}"!')
    video_data = await state.get_data()
    await state.clear()
    await add_video_url(user_id=message.from_user.id,
                        video_name=video_data['video_name'],
                        url=video_data['url'])
    print('Добавили данные в БД')
    await message.answer(text=f'Видео добавлено в список! \r\n\n'
                              f'Вот что удалось найти на данный момент: \r\n\n'
                              f'🤙 Название видео: {dict_video_info["video_name"]} \n'
                              f'🙉 Просмотры: {dict_video_info["views"]} \n'
                              f'🙊 Дата публикации: {dict_video_info["publication_date"]} \n'
                              f'🙈 Лайки: {dict_video_info["likes"]}👍\n')


async def process_cancel_command(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        await message.answer(text=LEXICON_RU['nothing_cancel'])
        return
    await state.clear()
    await message.answer(text=LEXICON_RU['cancel_video_add'])

from aiogram.types import Message, CallbackQuery


from lexicon.lexicon_ru import LEXICON_RU
from database.db_crud import get_list_video
from keyboards.favourite_list_inline_kb import create_video_list_kb, create_edit_list_kb


async def process_start_command(message: Message):
    await message.answer(text=f'{message.from_user.first_name}, {LEXICON_RU[message.text]}')


async def process_help_command(message: Message):
    await message.answer(LEXICON_RU[message.text])


async def process_video_list_command(message: Message):
    video_list = await get_list_video(message.from_user.id)
    if not video_list:
        await message.answer(text=LEXICON_RU['no_video_in_list'])
        return
    await message.answer(text=f'{LEXICON_RU[message.text]}',
                         reply_markup=create_video_list_kb(video_list))


async def process_edit_video_list(callback: CallbackQuery):
    video_list = await get_list_video(callback.from_user.id)
    await callback.message.edit_text(
            text=LEXICON_RU[callback.data],
            reply_markup=create_edit_list_kb(video_list))
    await callback.answer()


async def process_delete_video_press(callback: CallbackQuery):
    await callback.answer(text='Удалили ссылку')


async def process_cancel_redact_press(callback: CallbackQuery):
    await callback.message.edit_text(text=LEXICON_RU['cancel_redact_text'])
    await callback.answer()


async def not_correct_url(message: Message):
    await message.answer(text=LEXICON_RU['not_correct_url'])


async def send_echo(message: Message):
    await message.reply(text=f'Извините {message.from_user.first_name} {LEXICON_RU["echo_message"]}')



from typing import List

from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

from utils.callbackdata import VideoInfo
from lexicon.lexicon_ru import LEXICON_RU


def create_video_list_kb(args: List):
    keyboard_build: InlineKeyboardBuilder = InlineKeyboardBuilder()
    for video_name, url in args:
        keyboard_build.button(text=video_name,
                              callback_data=VideoInfo(url=url))

    keyboard_build.adjust(1)
    keyboard_build.row(
        InlineKeyboardButton(
            text=LEXICON_RU['edit_button'],
            callback_data='edit_video_list'),
        InlineKeyboardButton(
            text=LEXICON_RU['cancel_button'],
            callback_data='cancel_redact'),
        width=2)

    return keyboard_build.as_markup()


def create_edit_list_kb(args):
    keyboard_build: InlineKeyboardBuilder = InlineKeyboardBuilder()
    for video_name, url in args:
        keyboard_build.button(text=f'{LEXICON_RU["del"]} {video_name}',
                              callback_data=f'{url}delete')

    keyboard_build.row(InlineKeyboardButton(
        text=LEXICON_RU['cancel_button'],
        callback_data='cancel_redact'))
    keyboard_build.adjust(1)
    return keyboard_build.as_markup()

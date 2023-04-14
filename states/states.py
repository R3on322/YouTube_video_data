from aiogram.fsm.state import State, StatesGroup


class FSMFillInfo(StatesGroup):
    fill_url = State()
    fill_video_name = State()

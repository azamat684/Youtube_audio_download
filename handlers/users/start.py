from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext
from loader import dp


@dp.message_handler(CommandStart(),state="*")
async def bot_start(message: types.Message,state: FSMContext):
    await message.answer(f"Salom, {message.from_user.full_name}!")
    await state.finish()

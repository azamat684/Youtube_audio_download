from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from aiogram.dispatcher.filters import Text
from pytube import YouTube
from io import BytesIO


@dp.message_handler(Text(startswith="https"))
async def get_audio(message:types.Message):
    await message.answer("soon")
    link=message.text
    from io import BytesIO
    buffer=BytesIO()
    url=YouTube(link)
    if url.check_availability() is None:
        audio=url.streams.get_audio_only()
        audio.stream_to_buffer(buffer=buffer)
        buffer.seek(0)
        filename=url.title
        print("chiqdi")
        await message.answer_audio(audio=buffer,caption=filename)
        print("chiqdi")
    else:
        await message.answer("Xatolik")
        
    
  
  
  
  
# @dp.message_handler(Text(startswith="https://www.youtube.com/" or "https://www.youtu.be/" or "https://youtube.com/" or "https://youtu.be/" or "http://www.youtube.com/" or "http://www.youtu.be/" or "http://youtube.com/" or "http://youtu.be/"), state="*")
# async def get_audio(message:types.Message, state: FSMContext):
#     link = message.text
#     audio = await db.select_audio(link=link)
#     if audio is None:
#         msg = await message.reply(text="🔍")
#         buffer = BytesIO()
#         url = YouTube(link)
#         if url.check_availability() is None:
#             try:
#                 audio = url.streams.get_audio_only()
#                 audio.stream_to_buffer(buffer=buffer)
#                 buffer.seek(0)

#                 total_file_size = len(buffer.getbuffer())

#                 filename=url.title
#                 await msg.delete()
#                 loading = await message.answer(text=f"0% yuklanmoqda...")
#                 label = True
#                 while label:
#                     if buffer:
#                         label = False
#                     for i in range(1, total_file_size, total_file_size // 100):
#                         await loading.edit_text(text=f"{round(i / total_file_size, 2) * 100}%  yuklanmoqda...")
#                 await loading.edit_text(text="🔽 Yuborilmoqda...")
#                 await message.answer_chat_action(action="upload_audio")
#                 audio = await message.answer_audio(audio=buffer, caption=filename)
#                 await loading.delete()
#                 await db.add_audio(link=link, file_id=audio.audio.file_id, caption=audio.caption)
#             except KeyError:
#                 await message.answer(text="Qo'shiqni yuklashda xatolik yuz berdi! Keyinroq urinib ko'ring yoki boshqa link jo'nating.")
#         else:
#             await message.answer("<b><i>Uzr, xatolik yuz berdi! Keyinroq urinib ko'ring!</i></b>", parse_mode='HTML')
#     else:
#         await message.answer_chat_action(action="upload_audio")
#         audio = await message.answer_audio(audio=audio.get('file_id'), caption=audio.get('caption')) 
        
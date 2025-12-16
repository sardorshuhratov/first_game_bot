import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    # O'zgartirish kerak bo'lgan yagona joy:
    game_url = "https://funny-valkyrie-3c6615.netlify.app/"

    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🏀 O'yinni boshlash", web_app=WebAppInfo(url=game_url))]
    ])

    await message.answer(
        "<b>Basketbol 3D: Professional Edition</b>\n\n"
        "Koptokni xohlagan yo'nalishingizda otishingiz mumkin. "
        "Savatga tushirish uchun aniqlik va kuchni to'g'ri tanlang!",
        parse_mode="HTML",
        reply_markup=kb
    )

if __name__ == "__main__":
    print("Bot ishlayapti...")
    asyncio.run(dp.start_polling(bot))
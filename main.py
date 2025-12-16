import os
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
    # O'yin joylashgan URL (masalan, GitHub Pages yoki Replit orqali hosting qilingan)
    # Hozircha bu yerga o'z saytingiz manzilini qo'yishingiz kerak
    game_url = "https://sizning-saytingiz.uz/index.html"

    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🏀 O'yinni boshlash", web_app=WebAppInfo(url=game_url))]
    ])

    await message.answer(
        "<b>Basketbol 3D o'yiniga xush kelibsiz!</b>\n\nPastdagi tugmani bosing va koptokni barmog'ingiz bilan savatga otishga harakat qiling!",
        parse_mode="HTML",
        reply_markup=kb
    )


if __name__ == "__main__":
    import asyncio

    asyncio.run(dp.start_polling(bot))
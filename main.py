from aiogram import Bot, Dispatcher, types, executor
import os

API_TOKEN = os.getenv("TELEGRAM_TOKEN")  # Telegram bot tokeningiz

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Web-app link (sizning HTML/JS faylingizni host qilgan link)
WEB_APP_URL = "https://funny-valkyrie-3c6615.netlify.app/"

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    print(f"[LOG] {message.from_user.full_name} ({message.from_user.id}) started the bot")
    await message.reply("Salom! Basketball o'yinini o'ynash uchun /play buyrug'ini yuboring.")

@dp.message_handler(commands=['play'])
async def play_game(message: types.Message):
    print(f"[LOG] {message.from_user.full_name} ({message.from_user.id}) clicked /play")
    keyboard = types.InlineKeyboardMarkup()
    web_app_btn = types.InlineKeyboardButton(
        text="O'YINNI BOSHLASH 🏀",
        web_app=types.WebAppInfo(url=WEB_APP_URL)
    )
    keyboard.add(web_app_btn)
    await message.reply("Basketball o'yiniga xush kelibsiz! Pastdagi tugmani bosing:", reply_markup=keyboard)

# WebAppData qabul qilish
@dp.message_handler(content_types=types.ContentType.WEB_APP_DATA)
async def web_app_data_handler(message: types.Message):
    try:
        data = message.web_app_data.data
        print(f"[LOG] {message.from_user.full_name} ({message.from_user.id}) scored: {data} ball")
        await message.reply(f"Sizning natijangiz: {data} ball!")
    except Exception as e:
        print(f"[ERROR] WebAppData handler: {e}")
        await message.reply(f"Xatolik yuz berdi: {e}")

if __name__ == "__main__":
    print("[INFO] Bot is starting...")
    executor.start_polling(dp, skip_updates=True)

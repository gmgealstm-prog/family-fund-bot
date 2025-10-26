import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# توکن ربات را از متغیر محیطی می‌خوانیم
TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')

# تابعی که وقتی کاربر دستور /start را می‌زند اجرا می‌شود
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    welcome_message = f"سلام {user.first_name}! 🌺\nبه صندوق فامیلی ما خوش آمدید!"
    await update.message.reply_text(welcome_message)

# تابع اصلی
def main():
    # ساخت برنامه (Application) با توکن ربات
    application = Application.builder().token(TOKEN).build()

    # اضافه کردن هندلر برای دستور /start
    application.add_handler(CommandHandler("start", start_command))

    # شروع轮询 ربات (ربات شروع به گوش دادن به پیام‌ها می‌کند)
    print("ربات در حال اجراست...")
    application.run_polling()

if __name__ == '__main__':
    main()
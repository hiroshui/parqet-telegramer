from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import os

load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

async def log_user_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    print(f"User ID: {user.id} | Username: @{user.username}")
    await update.message.reply_text(
        f"👋 Hello @{user.username or 'Unknown'}!\n"
        f"Your telegram user-id is: {user.id}"
    )

if __name__ == "__main__":
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(MessageHandler(filters.ALL, log_user_id))
    print("Bot runs...")
    app.run_polling()
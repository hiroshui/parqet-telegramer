import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from upload import upload_pdf  # Stelle sicher, dass dies eine asynchrone Funktion ist
from dotenv import load_dotenv

load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
ALLOWED_USER = int(os.getenv("TELEGRAM_USER_ID"))
PARQET_ID = os.getenv("PARQET_ID")

async def handle_document(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ALLOWED_USER:
        await update.message.reply_text("Not authorized.")
        return

    print("Receive files...")

    file = await context.bot.get_file(update.message.document.file_id)
    filename = update.message.document.file_name
    file_path = f"/tmp/{filename}"
    await file.download_to_drive(file_path)

    await update.message.reply_text("📄 PDF received, upload to parqet...")
    try:
        await upload_pdf(file_path, parqet_id=PARQET_ID)  # Asynchrone Funktion korrekt aufrufen
        await update.message.reply_text("✅ Upload successful.")
    except Exception as e:
        await update.message.reply_text(f"❌ Error while uploading: {e}")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    doc_handler = MessageHandler(filters.Document.PDF, handle_document)
    app.add_handler(doc_handler)
    app.run_polling()

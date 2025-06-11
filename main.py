from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import os

# Auto-replies dictionary
auto_replies = {
    "hi": "Hello! How can I help you?",
    "help": "Here’s a list of things I can do...",
    "price": "The price is ₹499 only!"
}

# Async reply function
async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text.lower()
    for keyword, reply in auto_replies.items():
        if keyword in msg:
            await update.message.reply_text(reply)
            break

if __name__ == '__main__':
    TOKEN = os.getenv("BOT_TOKEN")
    if not TOKEN:
        print("Error: BOT_TOKEN environment variable not set")
        exit(1)

    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))
    app.run_polling()

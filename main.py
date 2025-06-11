from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# Customize your replies here
auto_replies = {
    "hi": "Hello! How can I help you?",
    "help": "Here’s a list of things I can do...",
    "price": "The price is ₹499 only!"
}

async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg_text = update.message.text.lower()
    for keyword, reply in auto_replies.items():
        if keyword in msg_text:
            await update.message.reply_text(reply)
            break

if __name__ == '__main__':
    import os
    TOKEN = os.environ.get("BOT_TOKEN")
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), auto_reply))
    app.run_polling()
  

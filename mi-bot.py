import os
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hola! Soy tu bot de Telegram dockerizado 😎")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Responde con el mismo texto que recibe
    if update.message and update.message.text:
        await update.message.reply_text(update.message.text)

def main():
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise RuntimeError("BOT_TOKEN no está definido. Asegúrate de ponerlo en .env o en -e BOT_TOKEN=...")

    app = Application.builder().token(token).build()

    # Comandos
    app.add_handler(CommandHandler("start", start))

    # Mensajes de texto normales
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("Bot corriendo con long polling...")
    app.run_polling()

if __name__ == "__main__":
    main()

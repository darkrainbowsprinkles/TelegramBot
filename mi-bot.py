import os
import requests
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

# ================================
# /start
# ================================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hola! Soy tu bot de Telegram dockerizado 😎\n"
        "Usa /precio para ver el precio de una criptomoneda (Bitcoin, Ether o Pepe)."
    )

# ================================
# /precio → muestra opciones
# ================================
async def precio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["Bitcoin", "Ether", "Pepe"]
    ]
    markup = ReplyKeyboardMarkup(
        keyboard,
        one_time_keyboard=True,
        resize_keyboard=True
    )

    await update.message.reply_text(
        "¿De qué moneda quieres el precio?\nElige una opción:",
        reply_markup=markup
    )

# ================================
# Manejador de elección de moneda
# ================================
async def handle_coin_choice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    text = update.message.text.strip()

    # Mapeo de nombre → símbolo en Binance
    mapping = {
        "Bitcoin": "BTCUSDT",
        "Ether": "ETHUSDT",
        "Pepe": "PEPEUSDT",
    }

    if text not in mapping:
        # Si no es una de las monedas del teclado, que lo maneje el echo normal
        return

    symbol = mapping[text]

    # Llamada a la API pública de Binance
    url = "https://api.binance.com/api/v3/ticker/price"
    params = {"symbol": symbol}

    try:
        resp = requests.get(url, params=params, timeout=10)
        if resp.status_code != 200:
            await update.message.reply_text(
                f"No pude obtener el precio de {text} en este momento (HTTP {resp.status_code}).",
                reply_markup=ReplyKeyboardRemove()
            )
            return

        data = resp.json()
        price_str = data.get("price")

        if price_str is None:
            await update.message.reply_text(
                f"La respuesta de Binance no contiene precio para {symbol}.",
                reply_markup=ReplyKeyboardRemove()
            )
            return

        # Formato amigable
        # Muchos símbolos son contra USDT, lo tomamos como "dólares"
        await update.message.reply_text(
            f"💰 Precio actual de *{text}* ({symbol}) en Binance:\n"
            f"{price_str} USDT",
            parse_mode="Markdown",
            reply_markup=ReplyKeyboardRemove()
        )

    except requests.RequestException as e:
        await update.message.reply_text(
            f"Ocurrió un error al conectar con Binance:\n{e}",
            reply_markup=ReplyKeyboardRemove()
        )

# ================================
# Echo (para cualquier otro texto)
# ================================
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.text:
        await update.message.reply_text(update.message.text)

# ================================
# main
# ================================
def main():
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise RuntimeError(
            "BOT_TOKEN no está definido. "
            "Asegúrate de ponerlo en .env o en -e BOT_TOKEN=..."
        )

    app = Application.builder().token(token).build()

    # Comandos
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("precio", precio))

    # Handler para las opciones del teclado (Bitcoin/Ether/Pepe)
    app.add_handler(
        MessageHandler(
            filters.TEXT & filters.Regex(r"^(Bitcoin|Ether|Pepe)$"),
            handle_coin_choice,
        )
    )

    # Echo para otros textos
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, echo)
    )

    print("Bot corriendo con long polling...")
    app.run_polling()

if __name__ == "__main__":
    main()


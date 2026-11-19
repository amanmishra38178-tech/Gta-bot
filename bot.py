#!/usr/bin/env python3
"""
GTA Clipping Studio — Simple Telegram Bot (@GTAClippingAIbot)
===========================================================
Sirf /start pe reply karta hai. Token BotFather se aayega,
isliye yahan direct mat likho — BOT_TOKEN env var use karo.

Run:  export BOT_TOKEN="tumhara_token"
      python bot.py
"""

import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Token BotFather dashboard / env se aayega (yahan hardcode MAT karo)
BOT_TOKEN = os.environ.get("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """/start command pe ye message jayega."""
    await update.message.reply_text(
        "👋 GTA Clipping Studio!\n\n"
        "YouTube link bhejo, 30 sec ka clip pao 🎬\n"
        "Link bhejo, clip le ao — No Download, No Space."
    )


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()


if __name__ == "__main__":
    main()

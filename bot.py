from telegram.ext import Application, CommandHandler
import os

# Legge il token dalle variabili d'ambiente su Render
TOKEN = os.environ.get("BOT_TOKEN")

# comando /start
async def start(update, context):
    await update.message.reply_text("Ciao! Sono il tuo bot 🚀 attivo 24/7 su Render")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()

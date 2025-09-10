from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os

# Replace with your bot token
BOT_TOKEN = os.getenv('BOT_TOKEN')

def start(update, context):
    update.message.reply_text("Hello! Send 'hi' to get the link.")

def reply_to_hi(update, context):
    text = update.message.text.lower()
    if text == "hi":
        update.message.reply_text("Here’s your link: https://google.com")

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    # /start command
    dp.add_handler(CommandHandler("start", start))

    # Reply to "hi"
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, reply_to_hi))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()

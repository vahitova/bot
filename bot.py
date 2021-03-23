from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler
from telegram import ReplyKeyboardMarkup


def echo(update, context):
    update.message.reply_text(update.message.text)

def help(update, context):
    update.message.reply_text(
        "Я пока не умею помогать... Я только ваше эхо.")

def start(update, context):
    reply_keyboard = [['/start', '/help']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    update.message.reply_text(
        "Привет! Я эхо-бот. Напишите мне что-нибудь, и я пришлю это назад!", reply_markup=markup)



def main():
    updater = Updater('1796737799:AAHlxHF7n8tYerY1Xz0j1tVUbid1RoCGjRQ', use_context=True)
    dp = updater.dispatcher
    text_handler = MessageHandler(Filters.text, echo)
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(text_handler)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
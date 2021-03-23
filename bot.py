from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler
from telegram import ReplyKeyboardMarkup
k = 0

def echo(update, context):
    global k
    mess = ['вы действительно мой самый лучший класс', 'Хотя нет, лучшая группа', 'Настоящие айтишники', 'Все у вас будет хорошо', 'Все получится', 'Вы все поступите', 
            'И как бы вы меня не троллили', 'Точнее мумитроллили', 'Я вас очень люблю!', 'А все потому что...']
    k += 1
    update.message.reply_text(mess[k%10])

def help(update, context):
    update.message.reply_text(
        "Екатерина Юрьевна спешит на помощь!")

def main():
    updater = Updater('1796737799:AAHlxHF7n8tYerY1Xz0j1tVUbid1RoCGjRQ', use_context=True)
    dp = updater.dispatcher
    text_handler = MessageHandler(Filters.text, echo)
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(text_handler)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

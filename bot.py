from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings


# Логирование
logging.basicConfig(format='%(asctime)s: %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )
# http://tg//socks?server=phobos.public.opennetwork.cc&port=1090&user=772114&pass=LHNHr5FX


def main():

    mybot = Updater(
        settings.API_KEY, request_kwargs=settings.PROXY)
#    mybot = Updater("949061631:AAEt-gfHLIIVAx6zMJE6lc5_Tq-BMH7-Ld0", request_kwargs=PROXY) Тату
#    mybot = Updater("986211591:AAGdtht0tdbgnhs3US7yKTK-KVLqCy_zeqk", request_kwargs=PROXY)
    logging.info('Старт бота')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', start_user))
    dp.add_handler(CommandHandler('boss', boss_info))

    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


def start_user(bot, update):
    text = 'Отдел организации эксплуатации технической инфраструктуры IT'
    print(text)
    update.message.reply_text(text)


def boss_info(bot, update):
    text = 'Королев Алексей Петрович\na.korolev@volga.rt.ru\nтел.:(831) 437-50-66'
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = update.message.text
    logging.info('User: %s, Chat id: %s, Message: %s', update.message.chat.last_name + ' ' + update.message.chat.first_name,
                                                       update.message.chat.id,
                                                       update.message.text
    )
    update.message.reply_text(update.message.chat.last_name +
                              ' ' + update.message.chat.first_name + ': ' + user_text)
                           

main()

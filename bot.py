import random
import logging

from telegram.ext import Updater , CommandHandler , MessageHandler, Filters, ConversationHandler
from game import start_game, game_play, let_game
import settings


logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def main():
    mybot = Updater(settings.API_KEY)  #Ваш API от телеграма
    dp = mybot.dispatcher

    game = ConversationHandler(
        entry_points=[
        MessageHandler(Filters.regex('^(123)$'), start_game)],
        states={
            'game' : [MessageHandler(Filters.text, game_play)],
            'letter_game': [MessageHandler(Filters.text, let_game)],
            
        },
        fallbacks=[]
    )

    dp.add_handler(game)
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle()



def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text('Для начала игры наберите 123')


main()
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from time import sleep
import parse

class Bot:
    def __init__(self):
        '''
        Creating all the required stuff after initialization.
        '''
        self.updater = Updater(token='token')
        self.dispatcher = self.updater.dispatcher

    @staticmethod
    def start(bot, update):
        '''
        Just a test method to be edited in future.
        '''
        bot.send_message(chat_id=update.message.chat_id, text="Hello, I'm a CatBot. I can send you cat pictures \
if you enter /cat")
        bot.send_message(chat_id=update.message.chat_id, text="Sometimes I'm sending same pictures, or not sending \
them at all, please, forgive me for that and enter the command one more time :c ( I'm in test mode yet )")

    @staticmethod
    def cat(bot, update):
        bot.send_message(chat_id=update.message.chat_id, text="Looking for some cat pictures...")
        sleep(3)
        bot.send_message(chat_id=update.message.chat_id, text="Here's what I found! Look at this!")
        try:
            bot.send_photo(chat_id=update.message.chat_id, photo=parse.p.parse())
        except:
            sleep(3)
            bot.send_photo(chat_id=update.message.chat_id, photo=parse.p.parse())
    def main(self):
        '''
        This is where all magic happens.
        '''
        print("Bot started working.")
        self.dispatcher.add_handler(CommandHandler('start', self.start))
        self.dispatcher.add_handler(CommandHandler('cat', self.cat))
        self.updater.start_polling()


CatBot = Bot()
if __name__ == '__main__':
    CatBot.main()

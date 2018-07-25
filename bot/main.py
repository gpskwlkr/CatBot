from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


class Bot:
    def __init__(self):
        '''
        Creating all the required stuff after initialization.
        '''
        self.updater = Updater(token='')
        self.dispatcher = self.updater.dispatcher

    @staticmethod
    def start(bot, update):
        '''
        Just a test method to be edited in future.
        '''
        bot.send_photo(chat_id=update.message.chat_id, photo="https://78.media.tumblr.com/60bea0e3d81398b23d02d2909a03893a/tumblr_pceei0uyhV1wmzeljo1_1280.jpg")

    def main(self):
        '''
        This is where all magic happens.
        '''
        print("Bot started working.")
        self.dispatcher.add_handler(CommandHandler('start', self.start))
        self.updater.start_polling()


CatBot = Bot()
if __name__ == '__main__':
    CatBot.main()

import logging
from time import sleep
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from emoji import emojize
from parse import p

# Enabling logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)


class Bot:
    def __init__(self):
        """Creating all the required stuff after initialization."""
        self.updater = Updater(token='token')
        self.dispatcher = self.updater.dispatcher

    @staticmethod
    def start(bot, update):
        """Just a test method to be edited in future."""
        update.message.reply_text("Hello, {}. I'm a CatBot. I can send you cat pictures if you enter /cat".format(update.message.from_user.first_name))
        update.message.reply_text(emojize("Sometimes I'm sending same pictures, or not sending them at all, please, forgive me\
for that and enter the command one more time :crying_cat_face: ( I'm in test mode yet )"))
        update.message.reply_text("To see all commands, use - /help\nInformation about Creator - /creator")

    @staticmethod
    def cat(bot, update):
        update.message.reply_text(emojize("Looking for some cat pictures... :speech_balloon:"))
        sleep(3)
        update.message.reply_text(emojize("Here's what I found! Look at this :purple_heart:! "))
        bot.send_photo(chat_id=update.message.chat_id, photo=p.parse())

    @staticmethod
    def creator(bot, update):
        update.message.reply_text(emojize('''I'm a CatBot, created by @gpskwlkr :panda_face:.
I love cats very much  ^~^
Contact with my Creator via FaceBook - https://www.facebook.com/gpskwlkr.
Or Vk - https://vk.com/gpskwlkr.
Or as I've already mentioned, Telegram - @gpskwlkr.
If you got any advises what else I need, or you spotted any problem - talk with him.
I'm open source, what means you can see my soul here:
https://github.com/gpskwlkr/CatBot :octopus:'''))

    @staticmethod
    def help(bot, update):
        update.message.reply_text(emojize('''Available commands:
/start - We can start everything from scratch.
/cat - I'll find random cat picture for you :heart_eyes_cat:.
/creator - I'll give you information about my Creator :panda_face:.
/help - I'll give you a list of all commands.''', use_aliases=True))

    @staticmethod
    def error(bot, update, error):
        """If we got any error - log it then. We have to deal with it."""
        logger.warning("Update '%s' caused '%s' error" % (update, error))

    @staticmethod
    def unknown(bot, update):
        update.message.reply_text("Sorry, I can't understand you. List of all commands I know - /help")

    def main(self):
        """This is where all magic happens"""
        print("Bot started working.")  # Debug
        self.dispatcher.add_handler(CommandHandler('start', self.start))
        self.dispatcher.add_handler(CommandHandler('cat', self.cat))
        self.dispatcher.add_handler(CommandHandler('creator', self.creator))
        self.dispatcher.add_handler(CommandHandler('help', self.help))
        self.dispatcher.add_handler(MessageHandler(Filters.command, self.unknown))
        self.dispatcher.add_error_handler(self.error)
        self.updater.start_polling()


CatBot = Bot()
if __name__ == '__main__':
    CatBot.main()

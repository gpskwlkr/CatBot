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
    def error_msg(bot, update):
        bot.send_message(chat_id=update.message.chat_id, text="Oops.. there was an error, please try again.")

    @staticmethod
    def error(bot, update, error):
        """If we got any error - log it then. We have to deal with it."""
        logger.warning("Update '%s' caused '%s' error" % (update, error))
        bot.send_message(chat_id=update.message.chat_id, text="Oops.. there was an error, please try again.")

    @staticmethod
    def unknown(bot, update):
        update.message.reply_text(emojize(
            "I'm a little kitten yet, I don't know so much :crying_cat_face: . List of all commands I know - /help"))

    @staticmethod
    def start(bot, update):
        """Just a test method to be edited in future."""
        update.message.reply_text("Hello, {}. I'm a CatBot. I can send you cat pictures if you enter /cat".format(
            update.message.from_user.first_name))
        update.message.reply_text(emojize("Sometimes I'm sending same pictures, or not sending them at all, please, forgive me\
for that and enter the command one more time :crying_cat_face: ( I'm in test mode yet )"))
        update.message.reply_text("To see all commands, use - /help\nInformation about creator - /creator")

    def cat(self, bot, update):
        print(update.message.from_user.username)
        update.message.reply_text(emojize("Looking for some cat pictures... :speech_balloon:"))
        sleep(3)
        update.message.reply_text(emojize("Here's what I found! Look at this :purple_heart:! "))
        try:
            bot.send_photo(chat_id=update.message.chat_id, photo=p.parse("cat"))
        except KeyError:
            self.error_msg(bot, update)

    @staticmethod
    def creator(bot, update):
        update.message.reply_text(emojize('''I'm a CatBot, created by @gpskwlkr :panda_face:.
I love cats very much  ^~^
Contact my creator via Facebook - https://www.facebook.com/gpskwlkr.
Vk - https://vk.com/gpskwlkr.
Email - giorgianakidze@outlook.com
Or as I've already mentioned, Telegram - @gpskwlkr.
If you have any ideas what else I need, or you spotted any problem - talk to him.
I'm open source, which means you can see my soul here:
https://github.com/gpskwlkr/CatBot :octopus:'''))

    '''
    Secret command section beginning, you can find it yourself and not read it here :p
    '''
    def panda(self, bot, update):
        print("PANDA FOUND BY - %s " % update.message.from_user.username)
        update.message.reply_text("Wow, how did you know that command? It's a secret! Tell no one! Here's your reward!")
        try:
            bot.send_photo(chat_id=update.message.chat_id, photo=p.parse("panda"))
        except KeyError:
            self.error_msg(bot, update)
    '''
    Secret command section end.
    '''
    @staticmethod
    def help(bot, update):
        update.message.reply_text(emojize('''Available commands:
/start - We can start everything from scratch.
/cat - I'll find random cat picture for you :heart_eyes_cat:.
/creator - I'll give you information about my creator :panda_face:.
/help - I'll give you a list of all commands.
Shh.. there's a secret command, an easter egg, tip : my creator.''', use_aliases=True))

    def main(self):
        """This is where all magic happens"""
        print("Bot started working.")  # Debug
        self.dispatcher.add_handler(CommandHandler('start', self.start))
        self.dispatcher.add_handler(CommandHandler('cat', self.cat))
        self.dispatcher.add_handler(CommandHandler('panda', self.panda))
        self.dispatcher.add_handler(CommandHandler('creator', self.creator))
        self.dispatcher.add_handler(CommandHandler('help', self.help))
        self.dispatcher.add_handler(MessageHandler(Filters.command, self.unknown))
        self.dispatcher.add_error_handler(self.error)
        self.updater.start_polling()


CatBot = Bot()
if __name__ == '__main__':
    CatBot.main()


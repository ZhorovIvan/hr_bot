from Frameworks.hr_telebot import TelegramBot
from Frameworks.settings import read_config
from Frameworks.mysql_schema import *


def main() -> None:

    config = read_config()
    userdata = UserData()
    bot = TelegramBot(config, userdata)
    bot.run()

if __name__ == "__main__":
    # try:
        main()
    # except Exception as e: #     
    # logging.fatal(e)
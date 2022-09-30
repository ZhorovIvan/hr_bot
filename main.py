from Frameworks.hr_telebot import TelegramBot
from Frameworks.settings import read_config


def main() -> None:

    config = read_config()
    bot = TelegramBot(config)
    bot.run()

if __name__ == "__main__":
    # try:
        main()
    # except Exception as e: #     
    # logging.fatal(e)
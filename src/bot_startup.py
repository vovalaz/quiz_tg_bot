import asyncio

from telebot import asyncio_filters

from init_db import init_db  # noqa
from telegram import message_handlers  # noqa
from telegram.bot import bot

if __name__ == "__main__":
    # init_db()
    bot.add_custom_filter(asyncio_filters.StateFilter(bot))
    asyncio.run(bot.polling())
    bot.close()

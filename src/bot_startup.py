import asyncio

from telegram import message_handlers  # noqa

from telebot import asyncio_filters

from telegram.bot import bot
from init_db import init_db  # noqa


if __name__ == "__main__":
    # init_db()
    bot.add_custom_filter(asyncio_filters.StateFilter(bot))
    asyncio.run(bot.polling())
    bot.close()

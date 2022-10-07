import aiogram.types
from aiogram import Router

import config
from models import User


def setup():
    router = Router()
    router.message.register(filter_message)
    return router


async def filter_message(msg: aiogram.types.Message, bot: aiogram.Bot):
    if not await User.get(msg.from_user.id):
        await msg.delete()
        if msg.text:
            for a in config.ADMIN_IDS:
                try:
                    await bot.send_message(a, f'Сообщение от {msg.from_user.full_name} ({msg.from_user.id}) удалено.\n'
                                       f'Текст: {msg.text}')
                except:
                    pass
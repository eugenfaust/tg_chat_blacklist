from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.fsm.storage.memory import MemoryStorage

import config
from handlers import errors
from handlers import user

session = AiohttpSession()
bot_settings = {"session": session, "parse_mode": "HTML"}
ai_bot = Bot(token=config.MAIN_BOT_TOKEN, **bot_settings)

main_dispatcher = Dispatcher()

# routers
main_dispatcher.include_router(errors.setup())
main_dispatcher.include_router(user.setup())

from telebot.types import Message
from telebot import types
from .settings import bot, scheduler
from . import messages
from loguru import logger

scheduled_jobs = dict()

async def send_notification(telegram_id, message, add_keyboard=False):
    logger.info(f"{telegram_id=} {message=} {add_keyboard=}")
    if add_keyboard:
        keyboard = types.InlineKeyboardMarkup()
        ok_button = types.InlineKeyboardButton("Ок", callback_data='ok')
        keyboard.add(ok_button)
        await send_message(telegram_id, message, reply_markup=keyboard)
    else:
        await send_message(telegram_id, message)

def schedule_notification(telegram_id, message):
    logger.info(f"{telegram_id=} {message=}")
    job = scheduler.add_job(send_notification, 'interval', args=(telegram_id, message, True), seconds=5)
    if telegram_id in scheduled_jobs:
        scheduled_jobs[telegram_id].remove()
    scheduled_jobs[telegram_id] = job

async def cancel_notification(telegram_id):
    logger.info(f"{telegram_id=}")
    if telegram_id in scheduled_jobs:
        scheduled_jobs[telegram_id].remove()
        del scheduled_jobs[telegram_id]
    await send_message(telegram_id, messages.NOTIFICATION_DISABLED)

async def send_message(telegram_id, message, reply_markup=None):
    logger.debug(f"{telegram_id=} {message=}")
    await bot.send_message(telegram_id,message,reply_markup=reply_markup)
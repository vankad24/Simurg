from .settings import bot
from . import messages as ms
from telebot.types import Message
from .db_functions import test_subscription

@bot.message_handler(commands=["start"])
async def handle_start_command(message: Message) -> None:
    # # Если пользователь новый - регистрируем его
    # if not user_exist(message.chat.id):
    #     create_user(message.chat.id, message.from_user.username)
    #     bot.send_message(message.chat.id, ms.WELCOME_MESSAGE, reply_markup=menu_markup)
    # else:
    #     bot.send_message(
    #         message.chat.id, ms.ALREADY_REGISTERED_MESSAGE, reply_markup=menu_markup
    #     )
    #     insert_step(ms.MENU_STEP, message.chat.id)
    await bot.send_message(message.chat.id, ms.WELCOME_MESSAGE)

@bot.message_handler(commands=["subscribe"])
async def subscribe_command(message: Message) -> None:
    test_subscription()

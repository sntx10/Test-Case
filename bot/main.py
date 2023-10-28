from .handlers import handle_msg
from .settings import dp, bot

dp.message_handler()(handle_msg)




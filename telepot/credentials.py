from dotenv import load_dotenv
import os

load_dotenv()

bot_token = os.getenv("BOT_TOKEN", "xxxxx:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
bot_user_name = os.getenv("BOT_USER_NAME", "vitqst_bot")
URL = os.getenv("URL", "https://example.com/{}")
SECRET_NUM = os.getenv("SECRET_NUM", "xxxx")

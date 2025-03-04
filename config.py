import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", '7680621096:AAH9ON_ca_aJU9iVY63X6wvXLR4v0Q-hlQ8')
    API_ID = int(os.environ.get("API_ID", '28094744'))
    API_HASH = os.environ.get("API_HASH", 'a75af4285edc7747c57bb19147ca0b9b')
    AUTH_USER = os.environ.get('AUTH_USERS','5680454765').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = "🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌"#Here You Can Change with Your Name  or any custom name or title you prefer

import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", '7607537749:AAFmdMM7ZUE2WzpMq7WOCPsCgLXqEiF5EcQ')
    API_ID = int(os.environ.get("API_ID", '25579552'))
    API_HASH = os.environ.get("API_HASH", 'ac24e438ff9a0f600cf3283e6d60b1aa')
    AUTH_USER = os.environ.get('AUTH_USERS','7725560481').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = "🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌"#Here You Can Change with Your Name  or any custom name or title you prefer

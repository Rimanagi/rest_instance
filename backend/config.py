from pathlib import Path

# URL = "t.me/rim_RestoClub_bot/RestoClub."
# URL = "https://127.0.0.1:8000"

CONFIG_DIR = Path(__file__).resolve().parent
PROJECT_PATH = CONFIG_DIR.parent

# URL
HOST = 'localhost'
PORT = 8000
URL = f'{HOST}:{PORT}'
HTTPS_URL = "https://rimanagi.github.io/rest_instance/"

# TG BOT
CAPTION = 'Текст главной страницы ресторана'
MEDIA_PATH = PROJECT_PATH / 'backend'/ 'bot' / 'media'
WELCOME_PICTURE_PATH = MEDIA_PATH / 'welcome-new-members2c33078cb67e4a128df23a7d3cc3dcdb.png'

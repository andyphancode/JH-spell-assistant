import requests
import pyyaml
from dotenv import load_dotenv

load_dotenv()


TOKEN = os.getenv('DISCORD_BOT_TOKEN')
APPLICATION_ID = os.getenv('DISCORD_APPLICATION_ID')
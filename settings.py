import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

TW_CLIENT_KEY = os.environ.get("TWITTERCK")
TW_CLIENT_KEY_SECRET = os.environ.get("TWITTERCKSECRET")
TW_ACCSESS_TOKEN = os.environ.get("TWITTERAT")
TW_ACCSESS_TOKEN_SECRET = os.environ.get("TWITTERATSECRET")

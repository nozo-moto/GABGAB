import os
from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
Twitter_API_KEY= os.environ.get("Twitter_API_KEY")
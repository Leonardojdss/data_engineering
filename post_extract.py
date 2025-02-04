from dotenv import load_dotenv
import os
from openai import OpenAI
import requests
import pandas as pd

load_dotenv()

# variaveis de ambiente reddit
REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT")

# variaveis de ambiente openai
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI()


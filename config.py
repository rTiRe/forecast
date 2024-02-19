import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    HOST = os.getenv("HOST", "localhost")
    PORT = os.getenv("PORT", 8000)
    API_KEY = os.getenv("API_KEY", None)
    URL = os.getenv("URL", None)

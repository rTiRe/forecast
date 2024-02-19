"""File with data."""

import os

from dotenv import load_dotenv

load_dotenv()

DEFAULT_PORT = 8000


class Config:
    """A config class."""

    host = os.getenv('HOST', 'localhost')
    port = os.getenv('PORT', DEFAULT_PORT)
    api_key = os.getenv('API_KEY', None)
    url = os.getenv('URL', None)

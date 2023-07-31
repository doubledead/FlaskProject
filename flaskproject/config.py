import os
from os import getenv
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class Config:
    TESTING = getenv("TESTING", "").lower() == "true"
    SECRET_KEY = getenv("SECRET_KEY")

    # SQLALCHEMY_DATABASE_URI = getenv("DATABASE_URL")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL") 
    if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SERVER_NAME = getenv("SERVER_NAME")

    # NITRADO_CLIENT_ID = getenv("NITRADO_CLIENT_ID")
    # NITRADO_REDIRECT_SECRET = getenv("NITRADO_SECRET")
    # NITRADO_REDIRECT_URI = getenv("NITRADO_REDIRECT_URI")
    # NITRADO_ACCESS_TOKEN = getenv("NITRADO_ACCESS_TOKEN")
    # NITRADO_REFRESH_TOKEN = getenv("NITRADO_REFRESH_TOKEN")

    REDDIT_USERNAME = getenv("REDDIT_USERNAME")
    REDDIT_CLIENT_ID = getenv("REDDIT_CLIENT_ID")
    REDDIT_CLIENT_SECRET = getenv("REDDIT_CLIENT_SECRET")
    REDDIT_REDIRECT_URI = getenv("REDDIT_REDIRECT_URI")

    LOG_FORMAT = getenv(
        "LOG_FORMAT", "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    LOG_LEVEL = getenv("LOG_LEVEL", "INFO")

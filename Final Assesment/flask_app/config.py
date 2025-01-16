import os

class Config:
    # Secret key used for securing sessions and cookies
    SECRET_KEY = 'f1991a94540d877757cefa345a2b385692bdb40c93bbf01e'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
import os


class Config:
    SECRET_KEY = '5782bcbca6b3bfd4d8af8ee656d775a0'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'johnnyjohnnyg1@gmail.com'
    MAIL_PASSWORD = 'Toto0515!'
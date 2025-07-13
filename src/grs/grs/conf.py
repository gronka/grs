# import firebase_admin
# import os
# from passlib.context import CryptContext
# from sqlalchemy.engine.url import URL
import toml
from typing import List


class LogLevel:
    VERBOSE = 10
    DEBUG = 20
    INFO = 30
    WARNING = 40
    ERROR = 50
    WTF = 60


class Conf:
    base_url: str = ''
    image_url: str = ''
    hosted_path: str = '.tethys/hosted'
    jwt_algorithm: str = 'HS256'
    jwt_algorithms: List[str] = ['HS256']
    jwt_lifetime_minutes: int = 15
    jwt_session_lifetime_days: int = 365
    log_level: int = LogLevel.VERBOSE
    env: str = ''
    root_dir: str = ''

    rab_exchange = ''
    rab_host = 'localhost'
    rab_user = 'papi'
    rab_password = '1234'

    smtp_host = ''
    smtp_user = ''
    email_errors = ''
    email_noreply = ''

    # pwds= CryptContext(schemes=['bcrypt'], deprecated='auto')

    def __init__(self):
        with open('.tethys//creds.toml', 'r')  as lf:
            pat = toml.loads(lf.read())
            self.env = pat['environment']['env']
            self.root_dir = pat['environment']['root_dir']

            self.smtp_host = pat['smtp']['host']
            self.smtp_pass = pat['smtp']['pass']
            self.smtp_user = pat['smtp']['user']
            from_domain = pat['smtp']['from_domain']
            self.email_errors = f'PushBoi <errors@{from_domain}>'
            self.email_noreply = f'PushBoi <no-reply@{from_domain}>'


conf = Conf()

print('Configuration loaded')
print(f'ENV: {conf.env}')
print(f'ROOT_DIR: {conf.root_dir}')
print(f'base url: {conf.base_url}')

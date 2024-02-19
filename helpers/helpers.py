import random, string
from datetime import datetime

def randomword(length) -> str:
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))


def add_log(f, message, verbose):
    f.writelines(f'{verbose} : [{datetime.now()}] >> [MESSAGE]: {message}\n')
   
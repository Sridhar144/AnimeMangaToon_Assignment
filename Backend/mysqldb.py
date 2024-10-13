from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
import os
DB_USER=os.getenv('DB_USER')
DB_HOST=os.getenv('DB_HOST')
DB_PASSWORD=os.getenv('DB_PASSWORD')
DB_PORT=os.getenv('DB_PORT')
DB_NAME=os.getenv('DB_NAME')
# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':DB_NAME,
        'USER':DB_USER,
        'PASSWORD':DB_PASSWORD,
        'HOST':DB_HOST,
        'PORT':DB_PORT

    }
}
import mysql.connector
database=mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    passwd=DB_PASSWORD
)
#perpare a cursor obj
cursorObject=database.cursor()
#creatw a database
cursorObject.execute("CREATE DATABASE animemangatoon")

print("done")
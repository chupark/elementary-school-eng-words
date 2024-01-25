import mysql.connector
from .. import config

settings = config.Settings()

mydb = mysql.connector.connect(
  host=settings.DB_URL,
  user=settings.DB_USER,
  password=settings.DB_PASSWD,
  database=settings.DB_NAME
)
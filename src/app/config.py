from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_URL: str = 'export DB_URL=YOUR_DB_URL'
    DB_USER: str = 'export DB_USER=YOUR_DB_USER'
    DB_PASSWD: str = 'export DB_PASSWD=YOUR_DB_PASSWD'
    DB_NAME: str = 'export DB_NAME=YOUR_DB_NAME'
    API_URL: str= 'export API_URL=YOUR_API_URL'
from pydantic import BaseSettings

class SettingsConfig(BaseSettings):
    DB_HOSTNAME : str
    DB_NAME : str
    DB_PORT : str
    DB_PASSWORD : str
    DB_USERNAME : str
    DB_URI : str
    SECRET_KEY  : str
    ALGORITHM : str
    ACCESS_TOKEN_EXPIRE_TIME  : int

    class Config:
        env_file = ".env"

settings = SettingsConfig()
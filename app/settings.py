from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    OPENAI_API_KEY: str = None
    MODEL_NAME: str = 'gpt-3.5-turbo'

    model_config = SettingsConfigDict(env_file='.env')


settings_dict = Settings().model_dump()
OPENAI_API_KEY = settings_dict['OPENAI_API_KEY']
MODEL_NAME = settings_dict['MODEL_NAME']

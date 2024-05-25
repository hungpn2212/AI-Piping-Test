from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)


class Settings(BaseSettings):
    DEBUG: bool = False
    OPENAI_API_KEY: str = None
    OPENAI_ORG_ID: str = None

    model_config = SettingsConfigDict(env_file=".env")

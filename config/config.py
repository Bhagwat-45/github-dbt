from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    github_key : str = Field(validation_alias='GITHUB_KEY')
    base_url : str = Field(validation_alias='DEFAULT_URL')

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

settings = Settings()

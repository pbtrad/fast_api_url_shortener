from pydantic import BaseSettings

from functools import lru_cache

# Settings is subclass of BaseSettings
class Settings(BaseSettings):
    env_name: str = "local"
    base_url: str = "http://localhost:8000"
    db_url: str = "sqlite:///./fast_api_url_shortener.db"


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    print(f"Loading settings for: {settings.env_name}")
    return settings
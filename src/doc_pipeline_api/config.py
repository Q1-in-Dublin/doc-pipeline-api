from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_prefix="DOC_")

    log_level: str = "INFO"
    data_path: Path = Path("data/sample_holdings.csv")

settings = Settings()
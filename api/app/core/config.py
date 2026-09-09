from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_nome: str = "Helpdesk API"
    app_versao: str = "1.0.0"
    ambiente: str = "dev"

    database_url: str = "mysql+pymysql://user:password@host:port/database"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = Settings()


# Para testar se o codigo acima está lendo do .env execute no caminho super-dev-09-helpdesk/api:
# py -c "from app.core.config import settings; print(settings.database_url)"

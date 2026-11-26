from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "Document Intelligence API"
    environment: str = "development"
    max_upload_bytes: int = 10 * 1024 * 1024
    allowed_extensions: str = ".txt,.md,.csv,.pdf"
    log_level: str = "INFO"
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    @property
    def extension_set(self) -> set[str]:
        return {x.strip().lower() for x in self.allowed_extensions.split(",") if x.strip()}

settings = Settings()

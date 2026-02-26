from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_ID: str = "cloud-project-workflow"
    TOPIC_ID: str = "asteroid-workflow-topic"
    DATASET: str = "etl_workflow"
    TABLE_NAME: str = "asteroids"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )


settings = Settings()

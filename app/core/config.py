from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "AI Assistant API"
    debug: bool = True
    openrouter_api_key: str 

    class Config:
        env_file = ".env"

settings = Settings()

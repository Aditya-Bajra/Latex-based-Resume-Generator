from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    GOOGLE_API_KEY: str
    GEMINI_MODEL: str = "models/gemini-1.5-pro-latest"
    LATEX_TEMPLATE_PATH: str = "sample_resume.tex"

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
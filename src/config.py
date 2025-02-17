from pydantic import BaseSettings

class Settings(BaseSettings):
    upload_limit: int = 10 * 1024 * 1024  # 10 MB
    image_output_format: str = "png"  # Options: png, jpeg
    output_directory: str = "./output"

    class Config:
        env_file = ".env"

settings = Settings()
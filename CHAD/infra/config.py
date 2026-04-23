import os

class Settings:
    ENV = os.getenv("ENV", "dev")

settings = Settings()

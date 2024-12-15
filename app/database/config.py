import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Settings:
  PROJECT_NAME:str = "Blog API"
  PROJECT_VERSION: str = "0.1.0"
    
  database_username: str = os.getenv("POSTGRES_USERNAME")
  database_password: str = os.getenv("POSTGRES_PASSWORD")
  database_hostname: str = os.getenv("POSTGRES_HOSTNAME", "localhost")
  database_port: str = os.getenv("POSTGRES_PORT", 5432)
  database_name: str = os.getenv("POSTGRES_DB", "blog")

settings = Settings()

import logging
import os

from dotenv import find_dotenv, load_dotenv

from .config import AppConfig, DatabaseConfig, EmailConfig, SupabaseConfig

logger = logging.getLogger(__name__)

load_dotenv(find_dotenv("../.env"), override=True, verbose=True)

def get_config() -> AppConfig:
    return AppConfig(
        DEBUG=os.getenv("DEBUG", "False") == "True",
        database=DatabaseConfig(
            host=os.environ["DB_HOST"],
            port=int(os.getenv("DB_PORT", "5432")),
            name=os.environ["DB_NAME"],
            user=os.environ["DB_USER"],
            password=os.environ["DB_PASSWORD"],
        ),
        email=EmailConfig(
            email=os.environ["EMAIL_HOST_USER"],
            password=os.environ["EMAIL_HOST_PASSWORD"],
        ),
        supabase=SupabaseConfig(
            url=os.environ["SUPABASE_URL"],
            key=os.environ["SUPABASE_SECRET_KEY"]
            )
        )

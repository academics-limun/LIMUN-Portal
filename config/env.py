import logging
import os

from dotenv import find_dotenv, load_dotenv

from .config import AppConfig, DatabaseConfig, SupabaseConfig

logger = logging.getLogger(__name__)

load_dotenv(find_dotenv("../.env"), override=True, verbose=True)

def get_config() -> AppConfig:
    return AppConfig(
        DEBUG=os.getenv("DEBUG", "False") == "True",
        database=DatabaseConfig(
            host=os.environ["DB_HOST"],
            port=int(os.environ["DB_PORT"]),
            name=os.environ["DB_NAME"],
            user=os.environ["DB_USER"],
            password=os.environ["DB_PASSWORD"],
        ),
        supabase=SupabaseConfig(
            url=os.environ["SUPABASE_URL"],
            key=os.environ["SUPABASE_KEY"]
            )
        )

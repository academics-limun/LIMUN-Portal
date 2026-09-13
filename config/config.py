from dataclasses import dataclass

@dataclass(frozen=True)
class DatabaseConfig:
    name: str
    user: str
    password: str
    host: str
    port: int

@dataclass(frozen=True)
class SupabaseConfig:
    url: str
    key: str

@dataclass(frozen=True)
class AppConfig:
    DEBUG: bool
    SECRET_KEY: str

    database: DatabaseConfig
    supabase: SupabaseConfig

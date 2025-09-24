from functools import lru_cache
from .config import Settings, settings

@lru_cache()
def get_settings() -> Settings:
    """
    Cached settings dependency
    Use lru_cache so we don't recreate settings object on every request
    """
    return settings

# Alternative: if you need fresh settings each time (e.g., for testing)
def get_fresh_settings() -> Settings:
    """Non-cached settings dependency for testing"""
    return Settings()
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List


class Settings(BaseSettings):
    # JWT Settings
    SECRET_KEY: str = "your-secret-key-change-this-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440  # 24시간
    
    # Database
    DATABASE_URL: str = "sqlite:///./app.db"
    
    # CORS (문자열로 받아서 속성으로 변환)
    ALLOWED_ORIGINS_STR: str = "http://localhost:5173,http://localhost:3000"
    
    model_config = SettingsConfigDict(env_file=".env")
    
    @property
    def ALLOWED_ORIGINS(self) -> List[str]:
        """콤마로 구분된 문자열을 리스트로 변환"""
        return [origin.strip() for origin in self.ALLOWED_ORIGINS_STR.split(',')]


settings = Settings()

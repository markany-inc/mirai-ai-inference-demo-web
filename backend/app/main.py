from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import settings
from .database import engine, Base
from .routers import auth_router

# 데이터베이스 테이블 생성
Base.metadata.create_all(bind=engine)

# FastAPI 앱 생성
app = FastAPI(
    title="MirAI Inference API",
    description="AI Object Detection Web Service",
    version="0.1.0"
)

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 등록
app.include_router(auth_router)


@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "Welcome to MirAI Inference API"}


@app.get("/api/health")
async def health_check():
    """서버 상태 확인"""
    return {"status": "healthy", "message": "Server is running"}

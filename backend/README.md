# MirAI Inference - Backend

FastAPI 기반 AI Object Detection Backend 서버입니다.

## 🚀 시작하기

### 1. 가상환경 생성 및 활성화

```bash
# Anaconda 가상환경 생성
conda create -n mirai-ai python=3.13 -y

# 가상환경 활성화
conda activate mirai-ai
```

### 2. 패키지 설치

```bash
cd backend
pip install -r requirements.txt
```

### 3. 환경 변수 설정

`.env` 파일을 생성하고 다음 내용을 추가하세요:

```env
SECRET_KEY=your-secret-key-change-this-in-production-09f26e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=1440
DATABASE_URL=sqlite:///./app.db
ALLOWED_ORIGINS=http://localhost:5173,http://localhost:3000
```

### 4. 데이터베이스 초기화 및 테스트 사용자 생성

```bash
python init_db.py
```

이 명령어로 `test/test` 계정이 자동으로 생성됩니다.

### 5. 서버 실행

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

서버가 실행되면 다음 주소로 접속 가능합니다:
- API 서버: http://localhost:8000
- API 문서 (Swagger UI): http://localhost:8000/docs
- API 문서 (ReDoc): http://localhost:8000/redoc

## 📝 API 엔드포인트

### 인증 API

| Method | Endpoint | 설명 | 인증 필요 |
|--------|----------|------|----------|
| POST | `/api/auth/login` | 로그인 (JWT 발급) | ❌ |
| GET | `/api/auth/me` | 현재 사용자 정보 | ✅ |

### 기타 API

| Method | Endpoint | 설명 | 인증 필요 |
|--------|----------|------|----------|
| GET | `/` | Root endpoint | ❌ |
| GET | `/api/health` | 서버 상태 확인 | ❌ |

## 🔐 테스트 계정

- **Username**: `test`
- **Password**: `test`
- **Email**: `test@example.com`

## 🧪 API 테스트

### 로그인

```bash
curl -X POST "http://localhost:8000/api/auth/login" \
  -H "Content-Type: application/json" \
  -d '{"username": "test", "password": "test"}'
```

### 사용자 정보 조회

```bash
curl -X GET "http://localhost:8000/api/auth/me" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## 📁 프로젝트 구조

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI 앱 진입점
│   ├── config.py            # 설정 관리
│   ├── database.py          # DB 연결
│   ├── models/              # SQLAlchemy 모델
│   │   ├── __init__.py
│   │   └── user.py
│   ├── schemas/             # Pydantic 스키마
│   │   ├── __init__.py
│   │   └── user.py
│   ├── routers/             # API 라우터
│   │   ├── __init__.py
│   │   └── auth.py
│   └── services/            # 비즈니스 로직
│       ├── __init__.py
│       └── auth.py
├── init_db.py               # DB 초기화 스크립트
├── requirements.txt
└── .env
```

## 🔧 기술 스택

- **Python 3.13**
- **FastAPI**: 웹 프레임워크
- **SQLAlchemy**: ORM
- **SQLite**: 데이터베이스
- **JWT (python-jose)**: 토큰 인증
- **Bcrypt (passlib)**: 비밀번호 해싱
- **Uvicorn**: ASGI 서버


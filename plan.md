# AI Inference Demo Web 프로젝트 계획서

## 📋 프로젝트 개요

**목표**: 이미지/비디오 업로드 → AI Object Detection → Bounding Box 결과 반환하는 웹 서비스

### 주요 요구사항
- ✅ 로그인/인증 시스템
- ✅ 이미지/비디오 처리
- ✅ ONNX Runtime 기반 AI Inference
- ✅ 내부망 → 외부망 확장 가능한 구조

---

## 🏗️ 기술 스택

### Backend (Python 기반)
| 기술 | 용도 | 비고 |
|------|------|------|
| **Python 3.13** | 프로그래밍 언어 | AI/ML 라이브러리 완벽 호환, 안정성과 성능 최적화 |
| **FastAPI** | 웹 프레임워크 | 빠르고 현대적, 비동기 지원, 자동 API 문서화 |
| **ONNX Runtime** | AI 모델 inference | 최적화된 추론 엔진 |
| **OpenCV (cv2)** | 이미지/비디오 처리 | Bounding box 그리기 |
| **Pillow** | 이미지 처리 보조 | 이미지 변환 및 조작 |
| **python-multipart** | 파일 업로드 처리 | FastAPI 파일 업로드 지원 |
| **python-jose** | JWT 인증 | 토큰 기반 인증 |
| **passlib[bcrypt]** | 비밀번호 해싱 | 보안 강화 |
| **SQLAlchemy + SQLite** | 데이터베이스 | 사용자 관리 (나중에 PostgreSQL로 확장 가능) |
| **uvicorn** | ASGI 서버 | FastAPI 실행 서버 |

### Frontend
| 기술 | 용도 |
|------|------|
| **React + TypeScript** | UI 프레임워크 |
| **Vite** | 빌드 도구 |
| **Axios** | API 통신 |
| **React Router** | 라우팅 |
| **TailwindCSS** | 스타일링 |

### 배포 (Phase 6)
| 기술 | 용도 |
|------|------|
| **Docker** | 컨테이너화 |
| **Nginx** | 리버스 프록시 |
| **Let's Encrypt** | HTTPS (외부망 접속 시) |

---

## 📁 프로젝트 구조

```
mirai-ai-inference-demo-web/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py              # FastAPI 앱 진입점
│   │   ├── config.py            # 설정 관리
│   │   ├── database.py          # DB 연결
│   │   ├── models/              # SQLAlchemy 모델
│   │   │   ├── __init__.py
│   │   │   └── user.py
│   │   ├── schemas/             # Pydantic 스키마
│   │   │   ├── __init__.py
│   │   │   ├── user.py
│   │   │   └── inference.py
│   │   ├── routers/             # API 라우터
│   │   │   ├── __init__.py
│   │   │   ├── auth.py          # 로그인/회원가입
│   │   │   └── inference.py     # AI inference
│   │   ├── services/            # 비즈니스 로직
│   │   │   ├── __init__.py
│   │   │   ├── auth.py          # JWT 토큰 관리
│   │   │   └── ai_inference.py  # ONNX 모델 처리
│   │   └── utils/
│   │       ├── __init__.py
│   │       └── image_processing.py  # bbox 그리기 등
│   ├── models/                  # ONNX 모델 파일
│   │   └── yolov8n.onnx        # 예시
│   ├── uploads/                 # 임시 업로드 파일
│   ├── requirements.txt
│   └── .env                     # 환경 변수
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Login.tsx
│   │   │   ├── ImageUpload.tsx
│   │   │   └── ResultViewer.tsx
│   │   ├── services/
│   │   │   └── api.ts           # API 호출
│   │   ├── App.tsx
│   │   └── main.tsx
│   ├── package.json
│   └── vite.config.ts
├── docker-compose.yml           # (Phase 6)
├── plan.md                      # 이 문서
└── README.md
```

---

## 🚀 구현 단계별 계획

### Phase 1: 개발 환경 및 기본 구조 (1-2일)

#### Backend 초기 설정
- [ ] Anaconda 가상환경 생성 (`conda create -n mirai-ai python=3.13 -y`)
- [ ] FastAPI 프로젝트 구조 생성
- [ ] `requirements.txt` 작성
- [ ] 기본 라우터 구조 생성
- [ ] Health check 엔드포인트 구현

#### Frontend 초기 설정
- [ ] Vite + React + TypeScript 프로젝트 생성
- [ ] TailwindCSS 설정
- [ ] 기본 라우팅 설정
- [ ] 레이아웃 컴포넌트 생성

---

### Phase 2: 인증 시스템 (2-3일)

#### 데이터베이스 설정
- [ ] SQLAlchemy 모델 생성 (User 테이블)
- [ ] DB 초기화 스크립트 작성
- [ ] 마이그레이션 설정 (선택사항)

#### Backend 인증 API
- [ ] 회원가입 엔드포인트 (`POST /api/auth/register`)
- [ ] 로그인 엔드포인트 (`POST /api/auth/login`)
  - JWT 토큰 발급
  - 비밀번호 검증
- [ ] 토큰 검증 미들웨어 구현
- [ ] 현재 사용자 정보 조회 (`GET /api/auth/me`)

#### Frontend 로그인 UI
- [ ] 로그인 페이지 구현
- [ ] 회원가입 페이지 구현
- [ ] 토큰 저장/관리 (localStorage)
- [ ] Protected Route 구현
- [ ] 자동 로그인 (토큰 유효성 검사)

---

### Phase 3: 이미지 업로드 및 기본 처리 (2-3일)

#### Backend 파일 업로드
- [ ] 이미지 업로드 엔드포인트 (`POST /api/upload`)
- [ ] 비디오 업로드 엔드포인트
- [ ] 파일 타입 검증 (MIME type)
- [ ] 파일 크기 제한 설정
- [ ] 임시 저장소 관리 (uploads 폴더)
- [ ] 업로드 파일 자동 삭제 로직

#### Frontend 업로드 UI
- [ ] 파일 선택 UI
- [ ] 드래그앤드롭 기능
- [ ] 업로드 진행 상태 표시
- [ ] 이미지 미리보기
- [ ] 파일 타입/크기 클라이언트 검증

---

### Phase 4: AI Inference 구현 (3-5일)

#### ONNX 모델 통합
- [ ] ONNX Runtime 설정 및 테스트
- [ ] 모델 로딩 및 초기화 (싱글톤 패턴)
- [ ] Inference 함수 구현
- [ ] 전처리 로직 (이미지 리사이즈, 정규화)
- [ ] 후처리 로직 (NMS, confidence threshold)
- [ ] 테스트 모델 다운로드 (예: YOLOv8)

#### 결과 처리
- [ ] Bounding box 그리기 (OpenCV)
- [ ] 레이블 및 confidence score 표시
- [ ] 결과 이미지 생성 및 저장
- [ ] 비디오 프레임별 처리 (선택사항)
- [ ] Inference 엔드포인트 (`POST /api/inference`)

#### Frontend 결과 표시
- [ ] 결과 이미지 표시 컴포넌트
- [ ] Bounding box 정보 테이블
- [ ] Detection 통계 표시
- [ ] 결과 다운로드 기능
- [ ] 여러 이미지 처리 이력 관리

---

### Phase 5: 최적화 및 안정화 (2-3일)

#### 성능 최적화
- [ ] 비동기 처리 개선
- [ ] 모델 로딩 캐싱
- [ ] 배치 추론 지원 (여러 이미지 동시 처리)
- [ ] 큐 시스템 도입 (Celery + Redis) - 선택사항
- [ ] 응답 속도 측정 및 로깅

#### 에러 핸들링
- [ ] 전역 예외 처리기 구현
- [ ] 로깅 시스템 구축
- [ ] 사용자 친화적 에러 메시지
- [ ] Frontend 에러 바운더리
- [ ] 재시도 로직 (네트워크 오류 시)

#### 테스트
- [ ] 단위 테스트 (pytest)
- [ ] API 엔드포인트 테스트
- [ ] Frontend 컴포넌트 테스트 (선택사항)

---

### Phase 6: 배포 준비 (추후 진행)

#### Docker 컨테이너화
- [ ] Backend Dockerfile 작성
- [ ] Frontend Dockerfile 작성
- [ ] docker-compose.yml 작성
- [ ] 환경 변수 설정 (.env 템플릿)
- [ ] 볼륨 마운트 설정

#### 외부망 접속 설정
- [ ] Nginx 리버스 프록시 설정
- [ ] HTTPS 설정 (Let's Encrypt)
- [ ] CORS 설정 (특정 도메인만 허용)
- [ ] 방화벽 설정
- [ ] Rate Limiting 구현
- [ ] 도메인 설정

---

## 📦 주요 라이브러리 버전

### backend/requirements.txt

```txt
# Web Framework
fastapi==0.122.0
uvicorn[standard]==0.34.0
python-multipart==0.0.20

# Authentication
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4

# Database
sqlalchemy==2.0.36

# Validation & Settings
pydantic==2.10.6
pydantic-settings==2.7.1

# AI & Image Processing
onnxruntime==1.21.1
opencv-python==4.11.0.86
pillow==11.1.0
numpy==2.2.3

# Utilities
python-dotenv==1.0.1
```

### frontend/package.json (주요 dependencies)

```json
{
  "dependencies": {
    "react": "^19.0.0",
    "react-dom": "^19.0.0",
    "react-router-dom": "^7.9.4",
    "axios": "^1.7.9"
  },
  "devDependencies": {
    "@types/react": "^19.0.0",
    "@types/react-dom": "^19.0.0",
    "@vitejs/plugin-react": "^4.3.4",
    "typescript": "^5.9.2",
    "vite": "^6.0.7",
    "tailwindcss": "^4.0.0",
    "autoprefixer": "^10.4.20",
    "postcss": "^8.4.49"
  }
}
```

---

## 🔐 보안 고려사항

### 인증 & 권한
- ✅ JWT 토큰 만료 시간 설정 (24시간 권장)
- ✅ Refresh Token 구현 (선택사항)
- ✅ 비밀번호 bcrypt 해싱 (cost factor: 12)
- ✅ 비밀번호 강도 정책 (최소 8자, 영문+숫자 조합)

### 파일 처리
- ✅ 파일 크기 제한 (예: 10MB)
- ✅ 파일 타입 화이트리스트 (jpg, png, mp4 등)
- ✅ 파일명 sanitization (보안 취약점 방지)
- ✅ 업로드 파일 자동 삭제 (처리 후)

### API 보안
- ✅ CORS 설정 (필요한 도메인만 허용)
- ✅ Rate Limiting (API 요청 제한)
- ✅ SQL Injection 방지 (SQLAlchemy ORM 사용)
- ✅ XSS 방지 (입력값 검증 및 sanitization)

### 배포 환경
- ✅ HTTPS 사용 (외부망 접속 시 필수)
- ✅ 환경 변수로 민감 정보 관리
- ✅ Secret Key 강력하게 설정
- ✅ 디버그 모드 비활성화 (프로덕션)

---

## 🌐 API 엔드포인트 설계

### 인증 API
| Method | Endpoint | 설명 | 인증 필요 |
|--------|----------|------|----------|
| POST | `/api/auth/register` | 회원가입 | ❌ |
| POST | `/api/auth/login` | 로그인 (JWT 발급) | ❌ |
| GET | `/api/auth/me` | 현재 사용자 정보 | ✅ |
| POST | `/api/auth/logout` | 로그아웃 | ✅ |

### Inference API
| Method | Endpoint | 설명 | 인증 필요 |
|--------|----------|------|----------|
| POST | `/api/inference/image` | 이미지 객체 탐지 | ✅ |
| POST | `/api/inference/video` | 비디오 객체 탐지 | ✅ |
| GET | `/api/inference/history` | 처리 이력 조회 | ✅ |
| GET | `/api/inference/result/{id}` | 결과 다운로드 | ✅ |

### 기타 API
| Method | Endpoint | 설명 | 인증 필요 |
|--------|----------|------|----------|
| GET | `/api/health` | 서버 상태 확인 | ❌ |
| GET | `/api/models` | 사용 가능한 모델 목록 | ✅ |

---

## 💾 데이터베이스 스키마

### User 테이블
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### InferenceHistory 테이블 (선택사항)
```sql
CREATE TABLE inference_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    file_name VARCHAR(255) NOT NULL,
    file_type VARCHAR(50) NOT NULL,
    model_name VARCHAR(100) NOT NULL,
    detection_count INTEGER DEFAULT 0,
    processing_time FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

---

## 🎯 다음 단계 (우선순위)

1. **✅ Phase 1**: 개발 환경 설정 (Backend + Frontend)
2. **✅ Phase 2**: 인증 시스템 구현
3. **✅ Phase 4**: AI Inference 핵심 기능 (Phase 3과 병행 가능)
4. **✅ Phase 3**: 파일 업로드 UI/UX
5. **✅ Phase 5**: 최적화 및 안정화
6. **⏳ Phase 6**: Docker 및 배포 (외부망 접속)

---

## 📝 추가 고려사항

### 확장 가능성
- 여러 AI 모델 지원 (모델 선택 기능)
- 실시간 웹캠 스트리밍 처리
- 배치 처리 기능 (여러 파일 동시 업로드)
- 사용자별 모델 커스터마이징

### 성능 개선
- Redis 캐싱
- CDN 활용 (정적 파일)
- WebSocket을 통한 실시간 진행 상태
- GPU 가속 (CUDA 지원)

### 모니터링
- 로그 수집 및 분석
- 사용량 통계
- 에러 트래킹 (Sentry 등)
- 성능 모니터링

---

## 🔧 개발 환경 설정 명령어

### Backend 설정
```bash
# Anaconda 가상환경 생성 및 활성화
cd backend

# Python 3.13 버전으로 가상환경 생성 (권장)
# Python 3.13: AI/ML 라이브러리 완벽 호환 + 안정성 + 성능 최적화
conda create -n mirai-ai python=3.13 -y

# 가상환경 활성화
conda activate mirai-ai

# 패키지 설치
pip install -r requirements.txt

# 서버 실행
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend 설정
```bash
cd frontend
npm install
npm run dev
```

---

## 📚 참고 자료

- [FastAPI 공식 문서](https://fastapi.tiangolo.com/)
- [ONNX Runtime 문서](https://onnxruntime.ai/docs/)
- [React 공식 문서](https://react.dev/)
- [TailwindCSS 문서](https://tailwindcss.com/docs)
- [YOLOv8 ONNX Export](https://docs.ultralytics.com/modes/export/)

---

**작성일**: 2025-12-02  
**버전**: 1.0  
**작성자**: Yonghye Kwon


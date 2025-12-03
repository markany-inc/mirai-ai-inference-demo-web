# 🚀 MirAI Inference 설치 및 실행 가이드

이 가이드는 로그인 기능까지 구현된 프로젝트를 로컬에서 실행하는 방법을 안내합니다.

## 📋 사전 요구사항

- **Python 3.13** (Anaconda 권장)
- **Node.js 18+** 및 npm
- **Git**

---

## 🔧 Backend 설정 및 실행

### 1단계: Backend 디렉토리로 이동

```bash
cd backend
```

### 2단계: Anaconda 가상환경 생성

```bash
# Python 3.13 가상환경 생성
conda create -n mirai-ai python=3.13 -y

# 가상환경 활성화
conda activate mirai-ai
```

### 3단계: Python 패키지 설치

```bash
pip install -r requirements.txt
```

설치되는 주요 패키지:
- FastAPI (웹 프레임워크)
- Uvicorn (ASGI 서버)
- SQLAlchemy (ORM)
- python-jose (JWT)
- passlib (비밀번호 해싱)

### 4단계: 환경 변수 설정

`backend/` 폴더에 `.env` 파일을 생성하고 다음 내용을 추가하세요:

```env
SECRET_KEY=your-secret-key-change-this-in-production-09f26e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=1440
DATABASE_URL=sqlite:///./app.db
ALLOWED_ORIGINS=http://localhost:5173,http://localhost:3000
```

### 5단계: 데이터베이스 초기화

```bash
python init_db.py
```

이 명령어는:
- SQLite 데이터베이스 생성
- 테스트 사용자 `test/test` 자동 생성

출력 예시:
```
✅ 테스트 사용자가 생성되었습니다!
   Username: test
   Password: test
   Email: test@example.com
```

### 6단계: Backend 서버 실행

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

서버가 실행되면:
- 🌐 API 서버: http://localhost:8000
- 📚 API 문서: http://localhost:8000/docs

---

## 🎨 Frontend 설정 및 실행

### 1단계: 새 터미널 열기

Backend 서버를 실행한 상태로 **새 터미널**을 열어주세요.

### 2단계: Frontend 디렉토리로 이동

```bash
cd frontend
```

### 3단계: Node.js 패키지 설치

```bash
npm install
```

설치되는 주요 패키지:
- React 19
- TypeScript
- Vite
- React Router
- Axios
- TailwindCSS

### 4단계: Frontend 개발 서버 실행

```bash
npm run dev
```

서버가 실행되면:
- 🌐 Frontend: http://localhost:5173

---

## 🎯 실행 확인

### 1. 브라우저에서 Frontend 접속

http://localhost:5173 으로 접속하세요.

### 2. 로그인 페이지 확인

로그인 페이지가 표시되어야 합니다.

### 3. 테스트 계정으로 로그인

```
Username: test
Password: test
```

### 4. 로그인 성공!

대시보드 페이지로 이동하면 다음 정보가 표시됩니다:
- 👤 사용자 정보
- 📧 이메일
- 🆔 User ID
- ✅ 계정 상태
- 📅 가입일

---

## 🧪 API 테스트 (선택사항)

### Swagger UI로 테스트

http://localhost:8000/docs 접속 후:

1. **POST /api/auth/login** 클릭
2. "Try it out" 버튼 클릭
3. Request body 입력:
```json
{
  "username": "test",
  "password": "test"
}
```
4. "Execute" 버튼 클릭
5. Response에서 `access_token` 확인

### curl로 테스트

```bash
# 로그인
curl -X POST "http://localhost:8000/api/auth/login" \
  -H "Content-Type: application/json" \
  -d '{"username": "test", "password": "test"}'

# 사용자 정보 조회 (토큰 필요)
curl -X GET "http://localhost:8000/api/auth/me" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

---

## 🔍 문제 해결

### Backend 포트 충돌

만약 8000번 포트가 이미 사용 중이라면:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8001
```

그리고 `frontend/src/services/api.ts` 파일에서 `API_BASE_URL`을 수정하세요:

```typescript
const API_BASE_URL = 'http://localhost:8001';
```

### Frontend 포트 충돌

`frontend/vite.config.ts` 파일에서 포트 변경:

```typescript
export default defineConfig({
  server: {
    port: 3000, // 원하는 포트로 변경
  }
})
```

### CORS 오류

Backend의 `.env` 파일에서 `ALLOWED_ORIGINS`에 Frontend URL 추가:

```env
ALLOWED_ORIGINS=http://localhost:5173,http://localhost:3000
```

### 로그인 실패

1. Backend 서버가 실행 중인지 확인
2. `python init_db.py`를 실행했는지 확인
3. 브라우저 콘솔에서 네트워크 오류 확인

---

## 📂 프로젝트 구조

```
mirai-ai-inference-demo-web/
├── backend/              # FastAPI Backend
│   ├── app/
│   │   ├── main.py      # 진입점
│   │   ├── config.py    # 설정
│   │   ├── database.py  # DB 연결
│   │   ├── models/      # DB 모델
│   │   ├── schemas/     # Pydantic 스키마
│   │   ├── routers/     # API 라우터
│   │   └── services/    # 비즈니스 로직
│   ├── init_db.py       # DB 초기화
│   ├── requirements.txt
│   └── .env
│
├── frontend/            # React Frontend
│   ├── src/
│   │   ├── components/  # React 컴포넌트
│   │   ├── services/    # API 통신
│   │   ├── App.tsx
│   │   └── main.tsx
│   ├── package.json
│   └── vite.config.ts
│
├── plan.md              # 프로젝트 계획서
└── SETUP_GUIDE.md       # 이 파일
```

---

## 🎉 완료!

이제 로그인 기능이 작동하는 웹 애플리케이션이 실행되었습니다! 🚀

### ✅ 구현된 기능

- JWT 기반 인증 시스템
- 로그인/로그아웃
- 토큰 관리 (localStorage)
- Protected Route (인증된 사용자만 접근)
- 대시보드

### 🚧 다음 단계 (plan.md 참고)

- 이미지/비디오 업로드
- AI Object Detection (ONNX Runtime)
- Bounding Box 결과 표시
- 처리 이력 관리

---

## 💡 유용한 명령어

### Backend 서버 중지

터미널에서 `Ctrl + C`

### Frontend 서버 중지

터미널에서 `Ctrl + C`

### 가상환경 비활성화

```bash
conda deactivate
```

### 데이터베이스 재생성

```bash
# backend 폴더에서
rm app.db        # 기존 DB 삭제
python init_db.py  # 새로 생성
```

---

**문제가 있거나 질문이 있으시면 언제든지 물어보세요!** 😊


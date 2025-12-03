# MirAI Inference - Frontend

React + TypeScript + Vite 기반 AI Object Detection 웹 애플리케이션입니다.

## 🚀 시작하기

### 1. 패키지 설치

```bash
cd frontend
npm install
```

### 2. 개발 서버 실행

```bash
npm run dev
```

서버가 실행되면 http://localhost:5173 으로 접속하세요.

### 3. 로그인

테스트 계정으로 로그인:
- **Username**: `test`
- **Password**: `test`

## 📦 빌드

```bash
npm run build
```

빌드된 파일은 `dist/` 폴더에 생성됩니다.

## 🎨 주요 기능

### ✅ 구현 완료
- 로그인 페이지 (JWT 인증)
- 토큰 관리 (localStorage)
- Protected Route (인증 필요한 페이지 보호)
- 대시보드 (사용자 정보 표시)
- 자동 로그아웃 (토큰 만료 시)

### 🚧 예정
- 이미지/비디오 업로드
- AI Object Detection
- Bounding Box 결과 표시
- 처리 이력 관리

## 📁 프로젝트 구조

```
frontend/
├── src/
│   ├── components/
│   │   ├── Login.tsx          # 로그인 페이지
│   │   ├── Dashboard.tsx      # 대시보드
│   │   └── ProtectedRoute.tsx # 보호된 라우트
│   ├── services/
│   │   └── api.ts             # API 통신 및 토큰 관리
│   ├── App.tsx                # 메인 앱 컴포넌트
│   ├── main.tsx               # 진입점
│   └── index.css              # 전역 스타일
├── index.html
├── package.json
├── vite.config.ts
└── tailwind.config.js
```

## 🔧 기술 스택

- **React 19**: UI 라이브러리
- **TypeScript**: 타입 안정성
- **Vite**: 빌드 도구
- **React Router**: 라우팅
- **Axios**: HTTP 클라이언트
- **TailwindCSS**: 스타일링

## 🌐 API 연동

Frontend는 Backend API와 다음과 같이 통신합니다:

- Backend URL: `http://localhost:8000`
- JWT 토큰은 localStorage에 저장
- 모든 API 요청에 자동으로 토큰 포함
- 401 에러 시 자동 로그아웃

## 🎯 라우팅

| 경로 | 컴포넌트 | 설명 | 인증 필요 |
|------|----------|------|----------|
| `/login` | Login | 로그인 페이지 | ❌ |
| `/dashboard` | Dashboard | 대시보드 | ✅ |
| `/` | - | Dashboard로 리다이렉트 | ✅ |




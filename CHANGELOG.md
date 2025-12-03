# Changelog

이 프로젝트의 모든 주요 변경 사항은 이 파일에 기록됩니다.

포맷은 [Keep a Changelog](https://keepachangelog.com/ko/)를 따르며, 버저닝은 [Semantic Versioning](https://semver.org/lang/ko/)을 준수합니다.

## [0.1.0] - 2025-12-03

### Added (추가됨)
- **Backend**
  - FastAPI 기본 구조 및 SQLite 데이터베이스 연동 설정
  - SQLAlchemy 모델 설계 (User)
  - JWT 기반 인증 시스템 (로그인, 회원가입, 토큰 갱신)
  - CORS 설정 및 기본 헬스 체크 API (`/api/health`)

- **Frontend**
  - React + Vite + TypeScript 프로젝트 초기화
  - Tailwind CSS 스타일링 환경 구성
  - Axios 기반 API 클라이언트 모듈 (`api.ts`)
  - React Router 라우팅 설정 (Public/Private Routes)
  - 로그인 페이지 UI 및 기능 구현
  - 대시보드 UI 기본 레이아웃 (헤더, 로고, 사용자 정보 표시)

### Changed (변경됨)
- **Dashboard**: 초기 데모용 안내 문구 제거 및 기본 레이아웃 정리


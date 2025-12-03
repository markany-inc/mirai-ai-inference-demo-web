"""
데이터베이스 초기화 및 테스트 사용자 생성 스크립트
"""
from app.database import SessionLocal, engine, Base
from app.models.user import User
from app.services.auth import get_password_hash

# 테이블 생성
Base.metadata.create_all(bind=engine)

# 세션 생성
db = SessionLocal()

try:
    # 기존 test 사용자 확인
    existing_user = db.query(User).filter(User.username == "test").first()
    
    if existing_user:
        print("🔄 기존 test 계정을 삭제합니다...")
        db.delete(existing_user)
        db.commit()
        print("✅ 기존 계정이 삭제되었습니다.")
    
    # 테스트 사용자 생성
    test_user = User(
        username="test",
        email="test@example.com",
        hashed_password=get_password_hash("test"),
        is_active=True
    )
    
    db.add(test_user)
    db.commit()
    db.refresh(test_user)
    
    print("✅ 테스트 사용자가 생성되었습니다!")
    print(f"   Username: test")
    print(f"   Password: test")
    print(f"   Email: test@example.com")

except Exception as e:
    print(f"❌ 오류 발생: {e}")
    db.rollback()
finally:
    db.close()

from sqlalchemy.orm import Session
from auth.models import User
from auth.security import hash_password, verify_password

def create_user(db: Session, email: str, password: str) -> User | None:
    if db.query(User).filter(User.email == email).first():
        return None
    user = User(email=email, hashed_password=hash_password(password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def authenticate_user(db: Session, email: str, password: str) -> User | None:
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user

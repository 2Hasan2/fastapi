from fastapi import APIRouter, HTTPException, Depends
from app.models import User
from app.database import SessionLocal
from app.auth import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
from app.dependencies import get_current_user

router = APIRouter()

@router.post("/register")
async def register(username: str, email: str, password: str):
    db = SessionLocal()
    user = db.query(User).filter(User.username == username).first()
    
    if user:
        raise HTTPException(status_code=400, detail="Username already exists")

    new_user = User(username=username, email=email, password_hash=generate_password_hash(password))
    db.add(new_user)
    db.commit()
    db.close()

    return {"msg": "User created successfully"}

@router.post("/login")
async def login(username: str, password: str):
    db = SessionLocal()
    user = db.query(User).filter(User.username == username).first()
    db.close()

    if not user or not check_password_hash(user.password_hash, password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return {"username": current_user.username, "email": current_user.email}

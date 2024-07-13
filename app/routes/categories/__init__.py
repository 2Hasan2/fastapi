from fastapi import APIRouter, HTTPException, Depends
from app.models import Category
from app.database import SessionLocal
from app.auth import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
from app.dependencies import get_current_user

router = APIRouter()


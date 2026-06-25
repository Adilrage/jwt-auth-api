from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.database import Base, engine, get_db
from app import schemas, crud, auth

Base.metadata.create_all(bind=engine)

app = FastAPI(title="JWT Authentication API", version="1.0.0")

@app.get("/")
def home():
    return {"message": "JWT Authentication API is running"}

@app.post("/register", response_model=schemas.UserResponse)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing_email = crud.get_user_by_email(db, user.email)
    existing_username = crud.get_user_by_username(db, user.username)

    if existing_email:
        raise HTTPException(status_code=400, detail="Email already registered")

    if existing_username:
        raise HTTPException(status_code=400, detail="Username already taken")

    return crud.create_user(db, user)

@app.post("/login", response_model=schemas.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud.get_user_by_username(db, form_data.username)

    if not user or not auth.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )

    access_token = auth.create_access_token(data={"sub": user.username})

    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/profile")
def profile():
    return {
        "message": "Protected profile endpoint",
        "status": "JWT authentication is working"
    }

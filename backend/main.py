from fastapi import FastAPI, UploadFile, Depends, HTTPException, Form, Query
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional

from auth import create_access_token, verify_token
from database import Base, engine, SessionLocal, User
from files import process_parquet, process_csv, process_hdf5

app = FastAPI()

# Configuración de CORS
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,         # Cambia a ["*"] para desarrollo si quieres
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Crear tablas en la base de datos
Base.metadata.create_all(bind=engine)

@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    db = SessionLocal()
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user or user.password != form_data.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token(data={"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}

@app.get("/data/parquet")
def get_parquet(user=Depends(verify_token)):
    print("Entré a get_parquet")
    return process_parquet()

@app.get("/data/csv")
def get_csv(user=Depends(verify_token)):
    return process_csv()

@app.get("/data/hdf5")
def get_hdf5(user=Depends(verify_token)):
    return process_hdf5()

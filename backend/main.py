from fastapi import FastAPI, UploadFile, Depends, HTTPException, Form, Query
from fastapi.security import OAuth2PasswordRequestForm
from typing import Optional

from auth import create_access_token, verify_token
from database import Base, engine, SessionLocal, User
from files import process_parquet, process_csv, process_hdf5


Base.metadata.create_all(bind=engine)
app = FastAPI()

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

#app.get("/data/parquet")
#def get_parquet():  # Eliminamos la dependencia del token
#   print("Entré a get_parquet")
#   return process_parquet()

@app.get("/data/csv")
def get_csv(user=Depends(verify_token)):
    return process_csv()

@app.get("/data/hdf5")
def get_hdf5(user=Depends(verify_token)):
    return process_hdf5()

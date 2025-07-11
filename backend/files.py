import pandas as pd
from fastapi import HTTPException
import os

DATA_DIR = "data"

def process_parquet():
    path = os.path.join(DATA_DIR, "serie_dolar_2023_2025.parquet")
    try:
        df = pd.read_parquet(path)
        return df.head(10).to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al procesar parquet: {str(e)}")

def process_csv():
    path = os.path.join(DATA_DIR, "serie_dolar_2023_2025.csv")
    try:
        df = pd.read_csv(path)
        return df.head(10).to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al procesar CSV: {str(e)}")

def process_hdf5():
    path = os.path.join(DATA_DIR, "serie_dolar_2023_2025.h5")
    try:
        with pd.HDFStore(path, mode='r') as store:
            key = store.keys()[0]  # usa la primera clave encontrada
            df = store[key]
            return df.head(10).to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al procesar HDF5: {str(e)}")


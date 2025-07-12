# generar_dolar_parquet.py

import pandas as pd
import numpy as np
import os

# Crear carpeta "data" si no existe
os.makedirs("data", exist_ok=True)

# Número de registros
N = 100_000

# Rango de fechas (timestamps aleatorios)
start_date = pd.Timestamp("2023-01-01")
end_date = pd.Timestamp("2025-12-31")

# Generar fechas aleatorias
random_dates = pd.to_datetime(np.random.uniform(start_date.value, end_date.value, N).astype("int64"))

# Generar valores de dólar aleatorios entre 860 y 1050
valores_dolar = np.random.uniform(860, 1050, N).round(2)

# Crear DataFrame
df = pd.DataFrame({
    "timestamp": random_dates,
    "valor_dolar": valores_dolar
})

# Ordenar por fecha
df = df.sort_values("timestamp").reset_index(drop=True)

# Guardar como Parquet en la carpeta "data"
output_path = "data/serie_dolar_2023_2025.parquet"
df.to_parquet(output_path, index=False)

print(f"✅ Archivo generado con éxito en: {output_path}")


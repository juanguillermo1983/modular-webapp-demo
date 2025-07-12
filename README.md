# modular-webapp-demo

# Procedimiento para crear, iniciar y detener el entorno virtual

Este proyecto utiliza un entorno virtual para gestionar las dependencias de Python de manera aislada. A continuación se detallan los pasos para crear, activar y desactivar el entorno virtual en tu máquina.

## 1. Crear el entorno virtual

Para crear el entorno virtual, abre una terminal y navega al directorio donde se encuentra el proyecto. Luego, ejecuta el siguiente comando:

```
python3 -m venv venv
```

Este comando creará una carpeta llamada \`venv\` en el directorio actual, que contendrá todos los archivos del entorno virtual.

## 2. Activar el entorno virtual

### En Linux:

Para activar el entorno virtual en sistemas Linux o macOS, ejecuta el siguiente comando:

```
source venv/bin/activate
```

Después de activar el entorno virtual, deberías ver el nombre del entorno (\`venv\`) en el prompt de la terminal, lo que indica que el entorno virtual está activo.

## 3. Instalar las dependencias

Una vez que el entorno virtual esté activado, puedes instalar todas las dependencias necesarias para el proyecto ejecutando el siguiente comando:

```
pip install -r requirements.txt
```

Esto instalará todas las bibliotecas y dependencias listadas en el archivo \`requirements.txt\`.


## 4. Crear la data de pruena 

```
python genera-data-parquet.py
```

## 5. Ejecutar el proyecto

Con el entorno virtual activado, ahora puedes ejecutar el proyecto o los scripts, como:

```
uvicorn main:app --reload
```

## 5. Desactivar el entorno virtual

Para desactivar el entorno virtual, simplemente ejecuta el siguiente comando:

```
deactivate
```

Este comando desactivará el entorno virtual y volverás al entorno global de Python en tu sistema.

---

Recuerda siempre activar el entorno virtual antes de trabajar en el proyecto y desactivarlo una vez que hayas terminado.


## 6. Probar la API Usando CURL


# 🔐 Autenticación y Uso de la API

## 1. Obtener un Token de Acceso

Para acceder a los endpoints protegidos, primero debes autenticarte y obtener un token JWT:

```bash
curl -X POST http://127.0.0.1:8000/login \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=demo&password=demo"
```

Respuesta esperada:

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

## 2. Acceder a Endpoints Protegidos

Usa el token en el header `Authorization` para hacer requests a los endpoints protegidos:

Ejemplo: Obtener datos en formato Parquet

```bash
curl -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." \
  http://127.0.0.1:8000/data/parquet
```

Respuesta exitosa (muestra las primeras 10 filas):

```json
[
  {"timestamp": "2023-01-02T05:21:34.165555968", "valor_dolar": 987.44},
  {"timestamp": "2023-01-14T10:36:24.096343808", "valor_dolar": 903.23},
  ...
]

```



# 🚀 Instrucciones para construir e iniciar el proyecto con Docker Compose

## 🐳 1. Requisitos previos

- Tener instalado Docker y Docker Compose.
- Estar ubicado en el directorio raíz del proyecto (`modular-webapp-demo`).

## 📁 Estructura esperada del proyecto

```
modular-webapp-demo/
├── backend/
│   ├── main.py
│   ├── auth.py
│   ├── files.py
│   ├── database.py
│   ├── ...
│   └── requirements.txt
├── frontend/
│   ├── src/
│   ├── index.html
│   ├── package.json
│   └── ...
├── docker-compose.yml
├── .dockerignore
└── README.md
```

## ⚙️ 2. Construir los contenedores

```bash
docker-compose build
```

Esto construirá las imágenes para `backend` y `frontend`.

## 🚀 3. Levantar los servicios

```bash
docker-compose up
```

Esto iniciará los servicios definidos en `docker-compose.yml`.

- El **backend** estará disponible en: [http://localhost:8000](http://localhost:8000)
- El **frontend** estará disponible en: [http://localhost:5173](http://localhost:5173)

## 🧪 4. Probar que el backend responde

Login:

```bash
curl -X POST http://localhost:8000/login \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=demo&password=demo"
```

## 🛑 5. Detener los servicios

Presiona `Ctrl + C` o en otra terminal:

```bash
docker-compose down
```

---

## 🐞 Problemas comunes

- Si el backend no responde, revisa que `main.py` esté configurado correctamente.
- Si hay error CORS en el frontend, asegúrate de que `main.py` tenga correctamente el middleware de CORS.
- Verifica puertos expuestos correctamente en `docker-compose.yml`.

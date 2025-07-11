
# create_user.py

from database import SessionLocal, Base, engine, User

def crear_usuario(username: str, password: str):
    # Crear tablas si no existen
    Base.metadata.create_all(bind=engine)

    # Crear sesión de DB
    db = SessionLocal()

    # Verificar si ya existe el usuario
    user_existente = db.query(User).filter(User.username == username).first()
    if user_existente:
        print(f"⚠️  El usuario '{username}' ya existe.")
        db.close()
        return

    # Crear usuario nuevo
    user = User(username=username, password=password)
    db.add(user)
    db.commit()
    db.close()
    print(f"✅ Usuario '{username}' creado exitosamente.")

if __name__ == "__main__":
    crear_usuario("demo", "demo")  # Puedes cambiar esto si quieres otros valores
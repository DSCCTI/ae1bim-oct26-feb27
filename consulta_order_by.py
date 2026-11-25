from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from crear_base_entidades import Veterinario
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# .order_by() ordena el resultado; aquí por apellidos de la A a la Z
veterinarios = session.query(Veterinario).order_by(Veterinario.apellidos).all()

print("Veterinarios ordenados por apellido")
for v in veterinarios:
    print("%s %s - Licencia: %s" % (v.apellidos, v.nombres, v.licencia))
    print("---------")
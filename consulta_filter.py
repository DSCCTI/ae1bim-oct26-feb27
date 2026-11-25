from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from crear_base_entidades import Consultorio
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# .filter() devuelve solo los registros que cumplen la condición:
# consultorios cuya especialidad es "Medicina general"
consultorios = session.query(Consultorio).filter(
    Consultorio.especialidad == "Medicina general").all()

print("Consultorios de Medicina general")
for c in consultorios:
    print("%s - Clínica: %s" % (c.nombre, c.clinica.nombre))
    print("---------")
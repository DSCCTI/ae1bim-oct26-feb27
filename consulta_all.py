from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from crear_base_entidades import Clinica
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# .all() devuelve una lista con TODAS las clínicas
clinicas = session.query(Clinica).all()

print("Clínicas y número de historias clínicas asociadas")
for clinica in clinicas:
    # se recorren los consultorios de la clínica y los veterinarios
    # de cada consultorio, y se cuentan sus historias clínicas
    total_historias = 0
    for consultorio in clinica.consultorios:
        for veterinario in consultorio.veterinarios:
            total_historias = total_historias + len(veterinario.historias)
    print("%s -> %d historias clínicas" % (clinica.nombre, total_historias))
    print("---------")
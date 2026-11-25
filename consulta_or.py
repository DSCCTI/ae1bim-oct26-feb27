from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_  # se importa el operador or

from crear_base_entidades import HistoriaClinica
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# or_ devuelve los registros que cumplen AL MENOS UNA condición:
# historias de la mascota "Luna" O cuyo diagnóstico contenga "itis"
historias = session.query(HistoriaClinica).filter(
    or_(HistoriaClinica.nombre_mascota == "Luna",
        HistoriaClinica.diagnostico.like("%itis%"))).all()

print("Historias de Luna o con diagnóstico que contiene 'itis'")
for h in historias:
    print("%s | %s | %s" % (h.nombre_mascota, h.fecha_atencion, h.diagnostico))
    print("---------")
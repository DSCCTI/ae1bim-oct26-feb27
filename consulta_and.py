from datetime import date

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_  # se importa el operador and

from crear_base_entidades import HistoriaClinica
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# and_ devuelve los registros que cumplen TODAS las condiciones:
# historias atendidas en noviembre de 2026 Y elaboradas por el veterinario con id 3
historias = session.query(HistoriaClinica).filter(
    and_(HistoriaClinica.fecha_atencion >= date(2026, 11, 1),
         HistoriaClinica.veterinario_id == 3)).all()

print("Historias de noviembre 2026 elaboradas por el veterinario 3")
for h in historias:
    print("%s | %s | Vet: %s %s" % (h.nombre_mascota, h.fecha_atencion,
                                    h.veterinario.nombres, h.veterinario.apellidos))
    print("---------")
from datetime import date

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importan las clases del archivo crear_base_entidades
from crear_base_entidades import Clinica, Consultorio, Veterinario, HistoriaClinica
# se importa la cadena de conexión
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# ---------- Clínicas ----------
clinica1 = Clinica(nombre="PetCare Loja", direccion="Av. Universitaria y 10 de Agosto, Loja",
                   veterinario_responsable="Dra. María Torres")
clinica2 = Clinica(nombre="Huellitas Quito", direccion="Av. Amazonas N24-120, Quito",
                   veterinario_responsable="Dr. Carlos Mena")
clinica3 = Clinica(nombre="VetSalud Cuenca", direccion="Calle Larga 5-40, Cuenca",
                   veterinario_responsable="Dra. Paola Vintimilla")

# ---------- Consultorios (cada uno con su clínica) ----------
cons1 = Consultorio(nombre="Consultorio 101", especialidad="Medicina general", clinica=clinica1)
cons2 = Consultorio(nombre="Consultorio 102", especialidad="Cirugía", clinica=clinica1)
cons3 = Consultorio(nombre="Consultorio 201", especialidad="Dermatología", clinica=clinica2)
cons4 = Consultorio(nombre="Consultorio 301", especialidad="Medicina general", clinica=clinica3)

# ---------- Veterinarios (cada uno con su consultorio) ----------
vet1 = Veterinario(nombres="Ana", apellidos="Jaramillo", correo="ana.jaramillo@petcare.ec",
                   licencia="VET-1001", consultorio=cons1)
vet2 = Veterinario(nombres="Luis", apellidos="Ordóñez", correo="luis.ordonez@petcare.ec",
                   licencia="VET-1002", consultorio=cons2)
vet3 = Veterinario(nombres="Sofía", apellidos="Paredes", correo="sofia.paredes@huellitas.ec",
                   licencia="VET-2001", consultorio=cons3)
vet4 = Veterinario(nombres="Jorge", apellidos="Cueva", correo="jorge.cueva@vetsalud.ec",
                   licencia="VET-3001", consultorio=cons4)

# ---------- Historias clínicas (cada una con su veterinario) ----------
hist1 = HistoriaClinica(fecha_atencion=date(2026, 10, 5), diagnostico="Otitis externa",
                        tratamiento="Gotas óticas por 7 días", nombre_mascota="Firulais", veterinario=vet1)
hist2 = HistoriaClinica(fecha_atencion=date(2026, 10, 12), diagnostico="Gastroenteritis",
                        tratamiento="Dieta blanda y suero oral", nombre_mascota="Michi", veterinario=vet1)
hist3 = HistoriaClinica(fecha_atencion=date(2026, 10, 20), diagnostico="Fractura de pata",
                        tratamiento="Cirugía y reposo 30 días", nombre_mascota="Rocky", veterinario=vet2)
hist4 = HistoriaClinica(fecha_atencion=date(2026, 11, 2), diagnostico="Dermatitis alérgica",
                        tratamiento="Antihistamínico y champú medicado", nombre_mascota="Luna", veterinario=vet3)
hist5 = HistoriaClinica(fecha_atencion=date(2026, 11, 8), diagnostico="Sarna",
                        tratamiento="Baños medicados semanales", nombre_mascota="Toby", veterinario=vet3)
hist6 = HistoriaClinica(fecha_atencion=date(2026, 11, 15), diagnostico="Control de vacunas",
                        tratamiento="Vacuna antirrábica", nombre_mascota="Max", veterinario=vet4)

# se agregan los objetos a la sesión (a la espera del commit)
session.add_all([clinica1, clinica2, clinica3,
                 cons1, cons2, cons3, cons4,
                 vet1, vet2, vet3, vet4,
                 hist1, hist2, hist3, hist4, hist5, hist6])

# se confirman las transacciones
session.commit()
print("Datos ingresados correctamente")
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, Date, ForeignKey

# se importa la cadena de conexión del archivo configuracion
from configuracion import cadena_base_datos

# se genera el enlace al gestor de base de datos (SQLite)
engine = create_engine(cadena_base_datos)

# Base es la superclase de todas las entidades
Base = declarative_base()


class Clinica(Base):
    __tablename__ = 'clinica'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    direccion = Column(String(150), nullable=False)
    veterinario_responsable = Column(String(100), nullable=False)

    # una clínica tiene muchos consultorios (relación 1 a N)
    consultorios = relationship("Consultorio", back_populates="clinica")

    def __repr__(self):
        return "Clínica: nombre=%s dirección=%s responsable=%s" % (
            self.nombre, self.direccion, self.veterinario_responsable)


class Consultorio(Base):
    __tablename__ = 'consultorio'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    especialidad = Column(String(50), nullable=False)
    # clave foránea obligatoria: cada consultorio pertenece a UNA clínica
    clinica_id = Column(Integer, ForeignKey('clinica.id'), nullable=False)

    clinica = relationship("Clinica", back_populates="consultorios")
    # un consultorio tiene uno o varios veterinarios
    veterinarios = relationship("Veterinario", back_populates="consultorio")

    def __repr__(self):
        return "Consultorio: nombre=%s especialidad=%s" % (
            self.nombre, self.especialidad)


class Veterinario(Base):
    __tablename__ = 'veterinario'
    id = Column(Integer, primary_key=True)
    nombres = Column(String(100), nullable=False)
    apellidos = Column(String(100), nullable=False)
    correo = Column(String(100), nullable=False, unique=True)
    licencia = Column(String(30), nullable=False, unique=True)
    # cada veterinario pertenece únicamente a un consultorio
    consultorio_id = Column(Integer, ForeignKey('consultorio.id'), nullable=False)

    consultorio = relationship("Consultorio", back_populates="veterinarios")
    # un veterinario elabora varias historias clínicas
    historias = relationship("HistoriaClinica", back_populates="veterinario")

    def __repr__(self):
        return "Veterinario: %s %s licencia=%s" % (
            self.nombres, self.apellidos, self.licencia)


class HistoriaClinica(Base):
    __tablename__ = 'historia_clinica'
    id = Column(Integer, primary_key=True)
    fecha_atencion = Column(Date, nullable=False)
    diagnostico = Column(String(200), nullable=False)
    tratamiento = Column(String(200), nullable=False)
    nombre_mascota = Column(String(50), nullable=False)
    # cada historia clínica la elabora obligatoriamente un veterinario
    veterinario_id = Column(Integer, ForeignKey('veterinario.id'), nullable=False)

    veterinario = relationship("Veterinario", back_populates="historias")

    def __repr__(self):
        return "Historia: mascota=%s fecha=%s diagnóstico=%s" % (
            self.nombre_mascota, self.fecha_atencion, self.diagnostico)


# se crean en la base de datos las tablas que aún no existan
Base.metadata.create_all(engine)
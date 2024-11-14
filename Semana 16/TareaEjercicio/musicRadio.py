from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class Artista(Base):
    __tablename__ = 'tbl_artista'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    genero = Column(String, nullable=False)
    
    #Artista con albumes
    albumes = relationship('Album', back_populates='artista')

class Album(Base):
    __tablename__ = 'tbl_album'
    
    id = Column(Integer, primary_key=True)
    titulo = Column(String, nullable=False)
    anio = Column(Integer, nullable=False)
    id_artista = Column(Integer, ForeignKey('tbl_artista.id'))
    
    #tabla Artista
    artista = relationship('Artista', back_populates='albumes')
    #Álbum con varias Canciones
    canciones = relationship('Cancion', back_populates='album')

class Cancion(Base):
    __tablename__ = 'tbl_cancion'
    
    id = Column(Integer, primary_key=True)
    titulo = Column(String, nullable=False)
    duracion = Column(Integer)  # duración en segundos
    id_album = Column(Integer, ForeignKey('tbl_album.id'))
    
    # Relación con la tabla Album
    album = relationship('Album', back_populates='canciones')

engine = create_engine('sqlite:///SpotYourMusic.db', echo=True)

# Creación de las tablas
Base.metadata.create_all(engine)

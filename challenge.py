from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, VARCHAR
from datos import datos, cin, registro

engine = create_engine('postgresql://postgres:password@localhost/alkemy')
Base = declarative_base()


class Turismo(Base):
    __tablename__ = 'Turismo'

    id = Column(Integer(), primary_key=True)
    cod_localidad = Column(VARCHAR())
    id_provincia = Column(Integer())
    id_departamento = Column(Integer())
    categoria = Column(String())
    provincia = Column(String())
    localidad = Column(String())
    nombre = Column(String())
    domicilio = Column(VARCHAR())
    codigo_postal = Column(VARCHAR())
    numero_de_telefono = Column(VARCHAR())
    mail = Column(VARCHAR())
    web = Column(VARCHAR())

    def __str__(self):
        return self.cod_localidad



class Salas_Cine(Base):
    __tablename__ = 'Salas_Cine'

    id = Column(Integer(), primary_key=True)
    provincia = Column(String())
    cantidad_de_pantallas = Column(VARCHAR())
    cantidad_de_butacas = Column(VARCHAR())
    cantidad_de_espacios_INCAA = Column(VARCHAR())

    def __str__(self):
        return self.provincia



class Registros(Base):
    __tablename__ = 'Registros'

    id = Column(Integer(), primary_key=True)
    categoria = Column(String())
    fuente = Column(VARCHAR())
    provincia_y_categoria = Column(String())

    def __str__(self):
        return self.categoria


Session = sessionmaker(engine)
session = Session()

if __name__ == '__main__':
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)



datos.to_sql('Turismo', if_exists='append', con=engine, index=False)
cin.to_sql('Salas_Cine', if_exists='append', con=engine, index=False)
registro.to_sql('Registros', if_exists='append', con=engine, index=False)


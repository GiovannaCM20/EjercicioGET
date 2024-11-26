from orm.config import BaseClass
from sqlalchemy import Column, String, Integer, DateTime, Float, ForeignKey
import datetime

class usuario(BaseClass):
    _tablename_="usuarios"
    id=Column(Integer, primary_key=True)
    nombre=Column(String(100))
    edad=Column(Integer)
    domicilio=Column(String(150))
    email=Column("email", String(100))
    password=Column(String(40))
    fecha_registro=Column(DateTime(timezone=True), default=datetime.datetime.now)


class Compra(BaseClass):
    __tablename__="compras"
    id=Column(Integer,primary_key=True)
    id_usuario=Column(Integer, ForeignKey(usuario.id))
    producto=Column(String(100))
    precio=Column(Float)
    
class Fotos(BaseClass):
    _tablename_="fotos"
    id=Column(Integer, primary_key=True)
    id_usuario=Column(Integer, ForeignKey(usuario.id))
    titulo=Column(String(100))
    descripcion=Column(String(200))
    ruta=Column(String(50))




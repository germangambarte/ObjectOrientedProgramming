from __main__ import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)


class Paquete(db.Model):
    __tablename__ = "paquete"
    id = db.Column(db.Integer, primary_key=True)
    numero_envio = db.Column(db.Integer)
    peso = db.Column(db.Integer)
    destinatario = db.Column(db.Text)
    entregado = db.Column(db.Boolean)
    observaciones = db.Column(db.Text)
    id_sucursal = db.Column(db.Integer, db.ForeignKey("sucursal.id"))
    id_transporte = db.Column(db.Integer, db.ForeignKey("transporte.id"))
    id_repartidor = db.Column(db.Integer, db.ForeignKey("repartidor.id"))


class Repartidor(db.Model):
    __tablename__ = "repartidor"
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer)
    nombre = db.Column(db.Text)
    dni = db.Column(db.Text)
    id_sucursal = db.Column(db.Integer, db.ForeignKey("sucursal.id"))
    comentario = db.relationship(
        "Comentario", backref="usuario", cascade="all, delete-orphan"
    )


class Sucursal(db.Model):
    __tablename__ = "sucursal"
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer)
    provincia = db.Column(db.Text)
    localidad = db.Column(db.Text)
    direccion = db.Column(db.Text)


class Transporte(db.Model):
    __tablename__ = "transporte"
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer)
    salida = db.Column(db.DateTime)
    llegada = db.Column(db.DateTime)
    id_sucursal = db.Column(db.Integer, db.ForeignKey("sucursal.id"))

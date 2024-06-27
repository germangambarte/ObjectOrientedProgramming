from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Sucursal(db.Model):
    __tablename__ = "sucursal"
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer, nullable=False)
    provincia = db.Column(db.String(30), nullable=False)
    localidad = db.Column(db.String(30), nullable=False)
    direccion = db.Column(db.String(60), nullable=False)
    repartidor = db.relationship(
        "Repartidor", backref="sucursal", cascade="all, delete-orphan"
    )
    transporte = db.relationship(
        "Transporte", backref="sucursal", cascade="all, delete-orphan"
    )
    paquete = db.relationship(
        "Paquete", backref="sucursal", cascade="all, delete-orphan"
    )

    def serialize(self):
        return dict(
            id=self.id,
            numero=self.numero,
            provincia=self.provincia,
            localidad=self.localidad,
            direccion=self.direccion,
            repartidor=self.repartidor,
            transporte=self.transporte,
            paquete=self.paquete,
        )


class Transporte(db.Model):
    __tablename__ = "transporte"
    id = db.Column(db.Integer, primary_key=True)
    numerotransporte = db.Column(db.Integer, nullable=False)
    fechahorasalida = db.Column(db.DateTime)
    fechahorallegada = db.Column(db.DateTime)
    idsucursal = db.Column(db.Integer, db.ForeignKey("sucursal.id"))
    paquete = db.relationship(
        "Paquete", backref="transporte", cascade="all, delete-orphan"
    )


class Repartidor(db.Model):
    __tablename__ = "repartidor"
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer, nullable=False)
    nombre = db.Column(db.String(60), nullable=False)
    dni = db.Column(db.String(8), nullable=False)
    idsucursal = db.Column(db.Integer, db.ForeignKey("sucursal.id"))
    paquete = db.relationship(
        "Paquete", backref="repartidor", cascade="all, delete-orphan"
    )


class Paquete(db.Model):
    __tablename__ = "paquete"
    id = db.Column(db.Integer, primary_key=True)
    numeroenvio = db.Column(db.Integer, nullable=False)
    peso = db.Column(db.Integer)
    nomdestinatario = db.Column(db.String(60), nullable=False)
    dirdestinatario = db.Column(db.String(100), nullable=False)
    entregado = db.Column(db.Boolean)
    observaciones = db.Column(db.Text)
    idsucursal = db.Column(db.Integer, db.ForeignKey("sucursal.id"))
    idtransporte = db.Column(db.Integer, db.ForeignKey("transporte.id"))
    idrepartidor = db.Column(db.Integer, db.ForeignKey("repartidor.id"))

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

from models import db

app = Flask(__name__)
app.config.from_pyfile("config.py")

db.init_app(app)

# sucursal_1 = Sucursal(numero=1,provincia="Buenos Aires", localidad="La Plata")
# sucursal_1 = Sucursal.c


@app.route("/")
def inicio():
    return render_template("inicio.html")


@app.route("/despachante", methods=["GET"])
def obtener_datos_despachante():
    return render_template("despachante-inicio.html")


@app.route("/despachante/seleccionar-sucursal", methods=["GET"])
def seleccionar_sucursal():
    sucursales = [
        {
            "codigo": "01",
            "provincia": "San Juan",
            "localidad": "Capital",
            "direccion": "direccion",
        },
        {
            "codigo": "02",
            "provincia": "San Juan",
            "localidad": "Sta Lucia",
            "direccion": "direccion",
        },
        {
            "codigo": "03",
            "provincia": "Mendoza",
            "localidad": "Capital",
            "direccion": "direccion",
        },
        {
            "codigo": "04",
            "provincia": "Mendoza",
            "localidad": "Tupungato",
            "direccion": "direccion",
        },
        {
            "codigo": "05",
            "provincia": "Cordoba",
            "localidad": "Capital",
            "direccion": "direccion",
        },
    ]
    return render_template("seleccionar-sucursal.html", sucursales=sucursales)


@app.route("/despachante/<int:sucursal>/registrar-paquete", methods=["GET", "POST"])
def registrar_paquete():
    sucursal = request.form.get("sucursal")
    if request.method == "POST":
        if (
            request.form["destino"]
            and request.form["destinatario"]
            and request.form["peso"],
        ):
            print("Todo bien")

        return render_template("registrar-paquete.html")
    else:
        return render_template("registrar-paquete.html", sucursal=sucursal)


if __name__ == "__main__":
    app.run(debug=True, port=8080)

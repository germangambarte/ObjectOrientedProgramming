from datetime import datetime

from flask import Flask, flash, redirect, render_template, request, session

from models import Paquete, Sucursal, Transporte, db

app = Flask(__name__)
app.config.from_pyfile("config.py")

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def inicio():
    session["sucursal"] = ""
    sucursales = Sucursal.query.order_by(Sucursal.numero).all()
    return render_template("inicio.html", sucursales=sucursales)


@app.route("/despachante", methods=["GET"])
def menu_despachante():
    session["sucursal"] = request.args.get("sucursal")
    return render_template("menu-despachante.html")


@app.route("/despachante/registro-paquete", methods=["GET", "POST"])
def registrar_paquete():
    if request.method == "POST":
        if (
            request.form.get("destino") == ""
            or request.form.get("destinatario") == ""
            or request.form.get("peso") == ""
        ):
            flash("Todos los campos son obligatorios", "error")
            return redirect("/despachante/registro-paquete")

        if session.get("sucursal") == "":
            flash("No seleccionó la sucursal en la que opera", "error")
            return redirect("/")

        numero_envio = 20

        ultimo_paquete = Paquete.query.order_by(Paquete.numeroenvio.desc()).first()
        if ultimo_paquete is not None:
            numero_envio = ultimo_paquete.numeroenvio + 20

        nuevo_paquete = Paquete(
            numeroenvio=numero_envio,
            peso=int(request.form.get("peso")),
            nomdestinatario=request.form.get("destinatario"),
            dirdestinatario=request.form.get("destino"),
            entregado=False,
            idrepartidor=0,
            idsucursal=session.get("sucursal"),
        )
        db.session.add(nuevo_paquete)
        db.session.commit()
        flash("El paquete se registró exitosamente", "success")
        return redirect("/despachante")

    else:
        return render_template("registro-paquete.html")


@app.route("/despachante/registro-salida", methods=["GET", "POST"])
def registro_salida():
    if request.method == "POST":
        if request.form.get("sucursal") == "" or request.form.getlist("paquete") == []:
            flash("Debe seleccionar al menos un paquete y una sucursal", "error")
            return redirect("/despachante/registro-salida")
        id_sucursal = request.form.get("sucursal")
        paquetes = request.form.getlist("paquete")

        nuevo_numero_transporte = 1

        ultimo_transporte = Transporte.query.order_by(
            Transporte.numerotransporte.desc()
        ).first()

        if ultimo_transporte is not None:
            nuevo_numero_transporte = ultimo_transporte.numerotransporte + 1

        nuevo_transporte = Transporte(
            numerotransporte=nuevo_numero_transporte,
            fechahorasalida=datetime.now(),
            fechahorallegada=None,
            idsucursal=id_sucursal,
        )

        db.session.add(nuevo_transporte)
        db.session.commit()

        for id in paquetes:
            paquete = Paquete.query.filter_by(id=id).first()
            if paquete:
                if paquete.idtransporte == 0:
                    paquete.idtransporte = nuevo_transporte.id
                    db.session.commit()

        flash("La salida del transporte se registró exitosamente", "success")
        return redirect("/despachante")

    else:
        sucursales = Sucursal.query.order_by(Sucursal.numero).all()
        paquetes = Paquete.query.filter_by(entregado=False, idrepartidor=0).all()
        return render_template(
            "registro-salida.html", sucursales=sucursales, paquetes=paquetes
        )


@app.route("/despachante/registro-llegada", methods=["GET", "POST"])
def registro_llegada():
    if request.method == "POST":
        id_transporte = request.form.get("transporte")
        transporte = Transporte.query.get(id_transporte)

        if transporte is None:
            flash("Debe seleccionar un transporte", "error")
            return redirect("/despachante/registro-llegada")

        transporte.fechahorallegada = datetime.now()

        db.session.commit()

        flash("La llegada del transporte se registró exitosamente", "success")
        return redirect("/despachante")
    else:
        transportes = Transporte.query.filter_by(
            fechahorallegada=None, idsucursal=session.get("sucursal")
        ).all()

        return render_template("registro-llegada.html", transportes=transportes)


if __name__ == "__main__":
    app.run(debug=True, port=8080)

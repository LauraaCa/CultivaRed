from flask import Blueprint, render_template, request, redirect, url_for, session
from config import get_connection  # Importar la conexión a PostgreSQL

# Crear el Blueprint con un nombre único
autenticacion_blueprint = Blueprint("autenticacion", __name__)

@autenticacion_blueprint.route("/")
def index():
    return render_template("inicio.html")

@autenticacion_blueprint.route("/Registro")
def registro():
    return render_template("/autenticacion/registro.html")

@autenticacion_blueprint.route("/IniciaSesion")
def iniciar():
    return render_template("/autenticacion/login.html")

@autenticacion_blueprint.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("autenticacion.index"))  # Asegúrate que el nombre coincide

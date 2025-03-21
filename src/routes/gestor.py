from flask import Flask, render_template, Blueprint, request, redirect, url_for, session
from config import get_connection  # Importamos la conexión a PostgreSQL

main = Blueprint('gestor_blueprint', __name__)


@main.route('/')
def gestor():
    if 'logueado' in session and session['logueado']:
        conn = get_connection()
        cur = conn.cursor()
        
        # Obtener datos del usuario autenticado
        cur.execute('SELECT * FROM usuarios WHERE email = %s', (session['email'],))
        user = cur.fetchone()
        
        cur.close()
        conn.close()

        if user:
            return render_template('gestor/perfilGestor.html', user=user)
        else:
            
            return """<script> alert("Usuario no encontrado."); window.location.href = "/CULTIVARED/login"; </script>"""
    
    return """<script> alert("Por favor, primero inicie sesión."); window.location.href = "/CULTIVARED/login"; </script>"""


@main.route('/gestionUsuarios', methods=['GET'])
def gestion_usuarios():
    if 'logueado' in session and session['logueado']:
        rol = request.args.get('rol' , 'all')
        conn = get_connection()
        cur = conn.cursor()
        
        if rol == 'all':
            cur.execute('SELECT id, nombre, apellido, genero, email, telefono, rol FROM usuarios')
        else:
             cur.execute('SELECT id, nombre, apellido, genero, email, telefono, rol FROM usuarios WHERE LOWER(rol) = %s', (rol.lower(),))    
            
        
        users = cur.fetchall()
        
         # Imprime los datos en la consola para depuración
        print("Usuarios obtenidos de la base de datos:")
        for user in users:
            print(user)
        cur.close()
        conn.close()

        return render_template('gestor/gestionUsuarios.html', users=users)
    else:
        return redirect(url_for('auth.login'))
from flask import Flask, render_template, Blueprint, request, redirect, url_for, session
from config import get_connection  # Importamos la conexión a PostgreSQL


# Definir el Blueprint antes de usarlo
main = Blueprint('admin_blueprint', __name__)

@main.route('/')
def admin():
    if 'logueado' in session and session['logueado']:
        conn = get_connection()
        cur = conn.cursor()
        
        # Obtener datos del usuario autenticado
        cur.execute('SELECT * FROM usuarios WHERE email = %s', (session['email'],))
        user = cur.fetchone()
        
        cur.close()
        conn.close()

        if user:
            return render_template('administrador/administrador.html', user=user)
        else:
            return """<script> alert("Usuario no encontrado."); window.location.href = "/CULTIVARED/login"; </script>"""
    
    return """<script> alert("Por favor, primero inicie sesión."); window.location.href = "/CULTIVARED/login"; </script>"""

# Definir la ruta de perfil
@main.route('/perfil')
def perfil():
    if 'logueado' in session and session['logueado']:
        conn = get_connection()
        cur = conn.cursor()
        
        # Obtener datos del usuario autenticado
        cur.execute('SELECT * FROM usuarios WHERE email = %s', (session['email'],))
        user = cur.fetchone()
        
        cur.close()
        conn.close()

        if user:
            return render_template('administrador/perfil.html', user=user)
        else:
            return """<script> alert("Usuario no encontrado."); window.location.href = "/CULTIVARED/login"; </script>"""
    
    return """<script> alert("Por favor, primero inicie sesión."); window.location.href = "/CULTIVARED/login"; </script>"""

# Definir la ruta de transacciones
@main.route('/transacciones')
def transacciones():
    if 'logueado' in session and session['logueado']:
        # Conecta a la BD y obtener el usuario actual
        conn = get_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM usuarios WHERE email = %s', (session['email'],))
        user = cur.fetchone()
        cur.close()
        conn.close()

        # user al render_template
        return render_template('administrador/transacciones.html', user=user)
    else:
        return """<script>alert("No estás logueado.");window.location.href="/CULTIVARED/login";</script>"""

# Definir la ruta de productos
@main.route('/productos')
def productos():
    if 'logueado' in session and session['logueado']:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM usuarios WHERE email = %s', (session['email'],))
        user = cur.fetchone()
        cur.close()
        conn.close()
        
        return render_template('administrador/productos.html', user=user)
    else:
        return """<script>alert("No estás logueado.");window.location.href="/CULTIVARED/login";</script>"""

# Definir la ruta de usuarios (crud)
@main.route('/crud')
def usuarios():
    if 'logueado' in session and session['logueado']:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM usuarios WHERE email = %s', (session['email'],))
        user = cur.fetchone()
        cur.close()
        conn.close()

        return render_template('administrador/usuarios.html', user=user)
    else:
        return """<script>alert("No estás logueado.");window.location.href="/CULTIVARED/login";</script>"""

# Definir la ruta de editar  
@main.route('/editar/<int:user_id>')
def editar(user_id):
    # Si quieres, verifica la sesión:
    if 'logueado' in session and session['logueado']:
        return """<h2>Página de edición del usuario con ID: {}</h2>
                  <p>Hacer.</p>""".format(user_id)
    else:
        return """<script>alert("No estás logueado");window.location.href="/CULTIVARED/login";</script>"""

from flask import Flask, flash, render_template, Blueprint, request, redirect, url_for, session
from config import get_connection  # Importamos la conexión a PostgreSQL

main = Blueprint('vendedor_blueprint', __name__)

@main.route('/')
def vendedor():
    if 'logueado' not in session or not session['logueado']:
        return """<script> alert("Por favor, primero inicie sesión."); window.location.href = "/CULTIVARED/login"; </script>"""

    conn = get_connection()
    cur = conn.cursor()

    # Obtener datos del usuario autenticado
    cur.execute('SELECT * FROM usuarios WHERE id = %s', (session['id'],))
    user = cur.fetchone()
    
    cur.close()
    conn.close()

    if user:
        return render_template('vendedor/vendedor.html', user=user)
    else:
        return """<script> alert("Usuario no encontrado."); window.location.href = "/CULTIVARED/login"; </script>"""

@main.route('/RegistroProductos')
def registro_productos():
    if 'logueado' not in session or not session['logueado']:
        return """<script> alert("Por favor, primero inicie sesión."); window.location.href = "/CULTIVARED/login"; </script>"""

    conn = get_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM usuarios WHERE id = %s', (session['id'],))
    user = cur.fetchone()
    cur.close()
    conn.close()

    return render_template('/vendedor/regitrosProducto.html', user=user)

@main.route('/formularioProductos', methods=['POST'])
def form():
    if 'id' not in session:
        flash("Por favor, inicie sesión.", "warning")
        return redirect(url_for('vendedor_blueprint.vendedor'))

    nombre = request.form.get('nombreProducto')
    descripcion = request.form.get('descripcionProducto')
    categoria = request.form.get('categoria')
    cantidad = request.form.get('unidades')
    precio = request.form.get('precio')
    idVendedor = session.get('id')

    if not all([nombre, descripcion, categoria, cantidad, precio]):
        flash("Todos los campos son obligatorios.", "danger")
        return redirect(url_for('vendedor_blueprint.registro_productos'))

    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO productos (nombre, descripcion, categoria, cantidad, precio, id_vendedor)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (nombre, descripcion, categoria, cantidad, precio, idVendedor))

        conn.commit()
        flash("Producto registrado correctamente.", "success")
    except Exception as e:
        conn.rollback()
        flash(f"Error al registrar el producto: {str(e)}", "danger")
    finally:
        cur.close()
        conn.close()

    return redirect(url_for('vendedor_blueprint.vendedor'))

@main.route('/MisProductos')
def mis_productos():
    if 'logueado' not in session or not session['logueado']:
        return """<script> alert("Por favor, primero inicie sesión."); window.location.href = "/CULTIVARED/login"; </script>"""

    conn = get_connection()
    cur = conn.cursor()         
    usuario_id = session['id']
    
    cur.execute('SELECT * FROM productos WHERE id_vendedor = %s', (usuario_id,))
    data = cur.fetchall()                       

    cur.execute('SELECT * FROM usuarios WHERE id = %s', (usuario_id,))
    user = cur.fetchone()
    
    cur.close()
    conn.close()

    return render_template('/vendedor/crudProductos.html', produ=data, user=user)

@main.route('/HistorialPedidos')
def historial_pedidos():
    if 'logueado' not in session or not session['logueado']:
        return """<script> alert("Por favor, primero inicie sesión."); window.location.href = "/CULTIVARED/login"; </script>"""

    return render_template('/vendedor/historialPedidos.html')

@main.route('/ResumenVentas')
def resumen_ventas():
    if 'logueado' not in session or not session['logueado']:
        return """<script> alert("Por favor, primero inicie sesión."); window.location.href = "/CULTIVARED/login"; </script>"""

    return render_template('/vendedor/resumenVentas.html')

@main.route('/MiPerfil')
def mi_perfil():
    if 'logueado' not in session or not session['logueado']:
        return """<script> alert("Por favor, primero inicie sesión."); window.location.href = "/CULTIVARED/login"; </script>"""

    conn = get_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM usuarios WHERE id = %s', (session['id'],))
    user = cur.fetchone()
    cur.close()
    conn.close()

    return render_template('/vendedor/perfilVendedor.html', user=user)

@main.route('/logout')
def logout():
    session.clear()  
    flash("Sesión cerrada correctamente.", "success")
    return redirect(url_for('autenticacion_blueprint.iniciar'))

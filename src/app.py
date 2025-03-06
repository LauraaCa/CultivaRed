from config import get_connection
from flask import Flask,render_template
from routes import autenticacion, admin, vendedor, comprador,gestor

app = Flask(__name__)
app.secret_key = 'clave_secreta_segura' 

def page_not_found(error):
    return "<h1>Not found page</h1>", 404

if __name__ == '__main__':
    app.register_blueprint(autenticacion.main, url_prefix='/CULTIVARED')
    app.register_blueprint(admin.main, url_prefix='/ADMINISTRADOR')
    app.register_blueprint(vendedor.main, url_prefix='/VENDEDOR')
    app.register_blueprint(comprador.main, url_prefix='/COMPRADOR')
    app.register_blueprint(gestor.main, url_prefix='/GESTOR')
    app.register_error_handler(404, page_not_found)
    app.run(debug=True)

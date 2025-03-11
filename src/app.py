from flask import Flask
from config import Config
from models import db

app = Flask(__name__)
app.config.from_object(Config)

# Inicializar la base de datos con Flask
db.init_app(app)

@app.route("/")
def home():
    return "🚀 ¡API de CultivaRed funcionando!"

# Crear las tablas antes de iniciar el servidor
with app.app_context():
    db.create_all()
    print("✅ Tablas creadas exitosamente.")

if __name__ == "__main__":
    app.run(debug=True)

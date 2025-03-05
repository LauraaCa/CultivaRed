from config import get_connection
from flask import Flask,render_template

app = Flask(__name__)

def page_not_found(error):
    return "<h1>Not found page</h1>", 404
    
@app.route('/')
def index():
    #conn = get_connection()
    return render_template('inicio.html')

if __name__ == '__main__':
    app.register_error_handler(404, page_not_found)
    app.run(debug=True)

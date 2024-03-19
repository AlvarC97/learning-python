from flask import Flask, render_template
from  database import con, cur 
import sqlite3
from flask import g #si la bd es vacio o si estoy en el lugar correcto

app = Flask(__name__)

DATABASE = 'market.db'

def get_db():
    db = getattr(g, '_database', None) #Identifica si hay bas  de datos o no
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is None:
        db.close() #Se cierra la base de datos

@app.route('/') #slash del localhost
def index():
    con = get_db
    cur.execute('SELECT * FROM users')
    data = cur.fetchall() #Guarda el resultado en data
    return render_template('index.html', data=data) #leguaje entendible para html

if __name__=='__main__':
    app.run(debug=True)

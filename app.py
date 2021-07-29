from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_dt import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

dt = FlaskDt(app, db, "display.html", "tables")

class Table1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)

class Table2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer, nullable=False)


@app.route('/home')
@app.route('/')
def home_page():
    return "Hello"

dt.display_table()

if __name__ == "__main__":
    app.run(debug=True)
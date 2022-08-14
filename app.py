from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_dt import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

dt = FlaskDt(db)

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

@app.route('/tables/<string:tablename>')
# @login_required
@dt.display_table
def table_page(**kwargs):
    tablename = kwargs.get('tablename', None)
    table_class = kwargs.get('table_class', None)
    columns = kwargs.get('columns', None)
    records = kwargs.get('records', None)

    if table_class:        
        return render_template('display.html', columns=columns, records=records, tablename=tablename)

    else:
        return f'No such table {tablename} in the database. Try creating the table'

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, request, make_response
from flask_migrate import Migrate
from models import db, Country
# from flask_restful import Api, Resource
# from werkzeug.exceptions import NotFound, Unauthorized
# from flask_cors import CORS
# from flask_bcrypt import Bcrypt

app = Flask(__name__)
# CORS(app)
# bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)


@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/image')
def image():
    return '<img src=https://images.unsplash.com/photo-1663256766998-dbda70037edf?q=80&w=2788&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D/>'

@app.route('/country/<string:title>')
def country(title):
    country = Country.query.filter(Country.title == title)
    country_response = {
        "name"
    }
    return f'<h1>{title}<h1>'

if __name__ == '__main__':
    app.run(debug=True)

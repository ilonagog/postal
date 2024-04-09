from flask import Flask, request, make_response, jsonify
from flask_migrate import Migrate
from models import db, Country
# from flask_restful import Api, Resource
# from werkzeug.exceptions import NotFound, Unauthorized
from flask_cors import CORS
# from flask_bcrypt import Bcrypt

app = Flask(__name__)
CORS(app)
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
from flask import jsonify

@app.route('/countries', methods=['GET'])
def get_countries():
    countries = Country.query.all()
    country_list = [{'name': country.name, 'code': country.code} for country in countries]
    return jsonify(country_list)


# @app.route('/country/<string:name>')
# def country(name):
#     country = Country.query.filter(Country.name == name).first()
#     if country:
#         country_response = {
#             "name": country.name,
#             "code": country.code
#         }
#         return country_response
#     else:
#         return make_response("Country not found", 404)


if __name__ == '__main__':
    app.run(debug=True)

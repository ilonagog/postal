from flask import Flask, request, make_response
from flask_migrate import Migrate
# from flask_restful import Api, Resource
# from werkzeug.exceptions import NotFound, Unauthorized
# from flask_cors import CORS
# from flask_bcrypt import Bcrypt

app = Flask(__name__)
# CORS(app)
# bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
from models import db

migrate = Migrate(app, db)
db.init_app(app)


@app.route('/')
def index():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)

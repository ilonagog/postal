from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.ext.hybrid import hybrid_property
# from app import bcrypt 
from datetime import datetime
metadata = MetaData()
db = SQLAlchemy(metadata=metadata)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    _password_hash = db.Column(db.String, nullable=False)
    admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @hybrid_property
    def password_hash(self):
        return self._password_hash

    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash, password.encode('utf-8'))

    def __repr__(self):
        return f'<User: ID: {self.id}, Username: {self.username}, Email: {self.email}, Admin: {self.admin}'


class Package(db.Model):
    __tablename__= "packages"

    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    tracking_number = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.String(200))
    weight = db.Column(db.Float)
    status = db.Column(db.String(20), default= "Pending")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship("User", backref=db.backref('packages'))

    def __repr__(self):
        return f'<Package: ID: {self.id}, Tracking Number: {self.tracking_number}, Status: {self.status}>'

class Shipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    package_id =  db.Column(db.Integer, db.ForeignKey('packages.id'), nullable=False)
    destination_country = db.Column(db.String, nullable=False)
    estimated_delivery_date =db.Column(db.DateTime)
    actual_delivery_date = db.Column(db.DateTime)
    status = db.Column(db.String, default='In transit')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    package= db.relationship('Package', backref=db.backref('shipments'))

  def __repr__(self):
        return f'<Shipment: ID: {self.id}, Package ID: {self.package_id}, Destination Country: {self.destination_country}, Status: {self.status}>'

class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name =  db.Column(db.String, unique=True, nullable=False)
    code = db.Column(db.String, unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Country: ID: {self.id}, Name: {self.name}, Code: {self.code}>'


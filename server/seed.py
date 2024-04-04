from app import app
from models import db, User, Package, Shipment, Country 

with app.app_context():
    User.query.delete()
    Package.query.delete()
    Shipment.query.delete()
    Country.query.delete()

    # user1 = User(username="ilona", email="ilona@gmail.com", password= "") 
  country1 = Country(name="")
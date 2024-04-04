from app import app
from models import db, User, Package, Shipment, Country 

with app.app_context():

    User.query.delete()
    Package.query.delete()
    Shipment.query.delete()
    Country.query.delete()

    # user1 = User(username="ilona", email="ilona@gmail.com", password= "") 
    country1 = Country(name="United States", code="US")
    country2 = Country(name ="Canada", code="CA")
    country3 = Country(name="United Kingsdom", code="UK")

    countries = [country1, country2, country3]

    db.session.add_all(countries)
    db.session.add(country1)
    db.session.commit()


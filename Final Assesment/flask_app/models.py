from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from app import login

# user class to manage the user's in the system
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
    return User.query.get(int(id)) # get user by their id

# StockItem class keeps track of the items in stock
class StockItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stock_code = db.Column(db.String(64), unique=True)
    quantity = db.Column(db.Integer)
    price = db.Column(db.Float)
    vat_rate = db.Column(db.Float, default=17.5)
    max_quantity = db.Column(db.Integer, default=100)
    last_updated = db.Column(db.DateTime, default=datetime.now)
    type = db.Column(db.String(50))  # Column to differentiate types

     # checks type, if it's StockItem or NavSys. helper for sqlAlchemy
    __mapper_args__ = {
        'polymorphic_identity': 'stock_item',
        'polymorphic_on': type
    }

    # STring representation of the stock item class
    def __str__(self):
        return (
            f"Stock Category: Car accessories\n"
            f"Stock Type: {self.get_stock_name()}\n"
            f"Description: {self.get_stock_description()}\n"
            f"StockCode: {self.stock_code}\n"
            f"PriceWithoutVAT: {self.price:.2f}\n"
            f"PriceWithVAT: {self.get_price_with_vat():.2f}\n"
            f"Total unit in stock: {self.quantity}\n"
            f"Total Value Without VAT: {self.get_total_value():.2f}\n"
            f"Total Value With VAT: {self.get_total_value(include_vat=True):.2f}\n"
            f"Stock Warning: {self.check_stock_level()}\n"
            f"Last Updated: {self.last_updated.strftime('%Y-%m-%d %H:%M:%S')}"
    )

    # get stock name
    def get_stock_name(self):
        return "Unknown Stock Name"

    #get stock description
    def get_stock_description(self):
        return "Unknown Stock Description"

    # get price with vat
    def get_price_with_vat(self):
        return self.price * (1 + self.vat_rate / 100)

    # get total value with or without vat
    def get_total_value(self, include_vat=False):
        price = self.get_price_with_vat() if include_vat else self.price
        return price * self.quantity

    # checks stock level
    def check_stock_level(self):
        if self.quantity < 5:
            return "Low stock: Consider restocking."
        elif self.quantity > 90:
            return "High stock: Might get overstocked."
        return "Stock levels are normal."

# NavSys, a type of stock item class
class NavSys(StockItem):
    brand = db.Column(db.String(64))

    # type mapper for sqlalchemy
    __mapper_args__ = {
        'polymorphic_identity': 'navsys',
    }

    # string representation of the navSys class
    def __str__(self):
        return super().__str__() + f"\nBrand: {self.brand}"

    def get_stock_name(self):
        return "Navigation System"

    def get_stock_description(self):
        return "GeoVision Sat Nav"
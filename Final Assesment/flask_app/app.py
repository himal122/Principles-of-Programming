from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from datetime import datetime

app = Flask(__name__)
# Load from the config class
app.config.from_object('config.Config')

# Set up the database connection
db = SQLAlchemy(app)

# Set up migration for database changes
migrate = Migrate(app, db)

# Set up login management for the app
login = LoginManager(app)

# specify login_view to redirect user to login
login.login_view = 'login'

from routes import *

# context processor for footer
@app.context_processor
def inject_datetime():
    return {'datetime': datetime}

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask
from flask.ext.mongoalchemy import MongoAlchemy
from config import Config
from views import author_bp


db = MongoAlchemy()
def create_app():
    app = Flask(__name__)
    print "0000000000"
    app.config.from_object(Config)
    print Config
    db.init_app(app)
    app.register_blueprint(author_bp)
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ozrnailnbimtbm:49350748a67a9cd86d6016f2d8fe39d9f6ae3c0da8382b8c2432069d1162f8f2@ec2-44-205-63-142.compute-1.amazonaws.com:5432/damdjjldc65r7p'
db = SQLAlchemy(app)

from App import routes
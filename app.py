from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///magia.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text, nullable=False)


def __repr__(self):
    return '<Article %r>' % self.id


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/pap")
def pap():
    return render_template("vtoria.html")


@app.route("/ka")
def KA():
    return render_template("KA.html")






if __name__ == "__main__":
    app.run(debug=True)

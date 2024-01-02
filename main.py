from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.root_path, 'models', 'cafes.db')
db = SQLAlchemy(app)


class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    map_url = db.Column(db.String(255), nullable=False)
    img_url = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(255), nullable=False)
    has_sockets = db.Column(db.Boolean, default=True)
    has_toilets = db.Column(db.Boolean, default=True)
    has_wifi = db.Column(db.Boolean, default=True)
    can_take_calls = db.Column(db.Boolean, default=True)
    seats = db.Column(db.String(255), nullable=False)
    coffee_price = db.Column(db.String(255), nullable=False)


cafe = Cafe()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/explorer')
def explorer():
    locations = db.session.query(Cafe.location).distinct().all()
    return render_template('explorer.html', locations=locations)


@app.route('/explore_loc/<location>')
def explore_loc(location):
    locations = db.session.query(Cafe.location).distinct().all()
    return render_template('explore_loc.html', locations=locations)


if __name__ == '__main__':
    app.run(debug=True)

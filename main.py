from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os
import json

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
button_states = {}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/explorer')
def explorer():
    locations = db.session.query(Cafe.location).distinct().all()
    return render_template('explorer.html', locations=locations, type=0)


@app.route('/explore_loc/<location>/<type>')
def explore_loc(location, type):
    if type == 1:

        return render_template('explore_loc.html', location=location)
    else:

        return render_template('explore_loc.html', location=location)


@app.route("/refresh_filters/<location>", methods=["POST"])
def refresh_filters(location):
    with open("models/filters.json", "r") as filters_file:
        filters_data = json.load(filters_file)

    action = request.form['action']
    if action == "like_button" and "like_button" not in filters_data["filters"]:
        filters = filters_data["filters"]
        filters.append("like_button")
        print(filters)
        filter_dict = {"filters": filters}
        with open("models/filters.json", "w") as filters_file_write:
            json.dump(filter_dict, filters_file_write, indent=4)

        return redirect(f'/explore_loc/{location}/1')
    # if action == "like_button" and "like_button" in filters:
    #     filters.remove("like_button")
    #     print(filters)
    #     return redirect(f'/explore_loc/{location}/1')
    else:
        return redirect(f'/explore_loc/{location}/0')


if __name__ == '__main__':
    app.run(debug=True)

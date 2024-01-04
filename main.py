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
    return render_template('explorer.html', locations=locations, way=0)


@app.route('/explore_loc/<location>/<way>')
def explore_loc(location, way):
    with open("models/filters.json", "r") as filters_file:
        filters_data = json.load(filters_file)
    print(way)
    if way == "1":
        print("chegou aqui")
        filters = filters_data["filters"]
        print(filters)
        return render_template('explore_loc.html', location=location, filters=filters)
    else:
        filters = []
        return render_template('explore_loc.html', location=location, filters=filters)


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

    elif action == "like_button" and "like_button" in filters_data["filters"]:
        filters = filters_data["filters"]
        filters.remove("like_button")
        print(filters)
        filter_dict = {"filters": filters}

        with open("models/filters.json", "w") as filters_file_write:
            json.dump(filter_dict, filters_file_write, indent=4)

    elif action == "sockets" and "sockets" not in filters_data["filters"]:
        filters = filters_data["filters"]
        filters.append("sockets")
        print(filters)
        filter_dict = {"filters": filters}
        with open("models/filters.json", "w") as filters_file_write:
            json.dump(filter_dict, filters_file_write, indent=4)

    elif action == "sockets" and "sockets" in filters_data["filters"]:
        filters = filters_data["filters"]
        filters.remove("sockets")
        print(filters)
        filter_dict = {"filters": filters}

        with open("models/filters.json", "w") as filters_file_write:
            json.dump(filter_dict, filters_file_write, indent=4)

    elif action == "toilets" and "toilets" not in filters_data["filters"]:
        filters = filters_data["filters"]
        filters.append("toilets")
        print(filters)
        filter_dict = {"filters": filters}

        with open("models/filters.json", "w") as filters_file_write:
            json.dump(filter_dict, filters_file_write, indent=4)

    elif action == "toilets" and "toilets" in filters_data["filters"]:
        filters = filters_data["filters"]
        filters.remove("toilets")
        print(filters)
        filter_dict = {"filters": filters}

        with open("models/filters.json", "w") as filters_file_write:
            json.dump(filter_dict, filters_file_write, indent=4)

    elif action == "wifi" and "wifi" not in filters_data["filters"]:
        filters = filters_data["filters"]
        filters.append("wifi")
        print(filters)
        filter_dict = {"filters": filters}

        with open("models/filters.json", "w") as filters_file_write:
            json.dump(filter_dict, filters_file_write, indent=4)

    elif action == "wifi" and "wifi" in filters_data["filters"]:
        filters = filters_data["filters"]
        filters.remove("wifi")
        print(filters)
        filter_dict = {"filters": filters}

        with open("models/filters.json", "w") as filters_file_write:
            json.dump(filter_dict, filters_file_write, indent=4)

    elif action == "calls" and "calls" in filters_data["filters"]:
        filters = filters_data["filters"]
        filters.remove("calls")
        print(filters)
        filter_dict = {"filters": filters}

        with open("models/filters.json", "w") as filters_file_write:
            json.dump(filter_dict, filters_file_write, indent=4)

    elif action == "calls" and "calls" not in filters_data["filters"]:
        filters = filters_data["filters"]
        filters.append("calls")
        print(filters)
        filter_dict = {"filters": filters}

        with open("models/filters.json", "w") as filters_file_write:
            json.dump(filter_dict, filters_file_write, indent=4)

    return redirect(f'/explore_loc/{location}/1')


if __name__ == '__main__':
    app.run(debug=True)

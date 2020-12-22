from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get(
    "DATABASE_URL", "sqlite:///heroku_trial.sqlite")

db = SQLAlchemy(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)


@app.route('/')
def index():
    return 'Hello World'


if __name__ == '__main__':
    app.run(debug=True)


@app.route('/api/tasks-postgres')
def taskPostGres():
    tasks = db.session.query(Task)
    data = []

    for task in tasks:
        item = {
            'id': task.id,
            'description': task.description
        }
        data.append(item)

    return jsonify(data)

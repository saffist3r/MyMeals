from flask import Flask, jsonify
from api.endpoints import meal
app = Flask(__name__)
app.register_blueprint(meal, url_prefix='/meals')


@app.route("/")
def main():
    return jsonify('MyMeals - API')

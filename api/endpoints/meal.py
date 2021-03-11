from flask import Blueprint, jsonify

meals = Blueprint('meal', __name__)


@meals.route('/')
def meal_tes():
    return jsonify("test")


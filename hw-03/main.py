from flask import Flask, Response
from webargs import fields, validate
from webargs.flaskparser import use_args
from services.student_generator import generate_student
from http import HTTPStatus
import json
import csv
import requests

app = Flask(__name__)


@app.route("/")
def index():
    return "<a href='/generate-students?count=1'>Generate students</a><hr><a href='/get-bitcoin-value?currency=USD&count=1'>Get bitcoin value</a>"


@app.route("/generate-students")
@use_args({
    "count": fields.Int(
        load_default=1,
        validate=validate.Range(min=1, max=1000)
    )},
    location="query"
)
def generate_students(args):
    students = [generate_student() for _ in range(args["count"])]
    with open("storage/students.csv", "w") as f:
        writer = csv.DictWriter(f, students[0].keys(), delimiter=";")
        writer.writeheader()
        writer.writerows(students)
    return students


@app.route('/get-bitcoin-value')
@use_args({
    "currency": fields.Str(
        load_default="USD",
    ),
    "count": fields.Int(
        load_default=1,
        validate=validate.Range(min=1)
    )},
    location="query"
)
def get_bitcoin_value(args):
    response = requests.get(f"https://bitpay.com/api/rates/{args['currency']}")
    if response.status_code != HTTPStatus.OK:
        return Response("Oops something went wrong!", status=response.status_code, mimetype="text/plain")
    bitcoin_rate = json.loads(response.content)
    return f"{bitcoin_rate["rate"] * args["count"]: 10.2f} ({args['currency']})"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)

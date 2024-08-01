from flask import Flask
from services.pwd_generator import PwdGenerator
import pandas as pd

app = Flask(__name__)


@app.route('/')
def index():
    return "<a href='/generate_password'>Generate password</a><hr><a href='/calculate_average'>CSV average</a>"


@app.route("/generate_password")
def generate_password():
    return f"Generated password is {PwdGenerator.hard(10, 20)}"


@app.route("/calculate_average")
def calculate_average():
    df = pd.read_csv("hw.csv", header=None, skiprows=1, names=["Index", "Height(Inches)", "Weight(Pounds)"])
    return f"Height(Inches): {df["Height(Inches)"].mean() : 10.2f}; Weight(Pounds): {df["Weight(Pounds)"].mean() : 10.2f}"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)
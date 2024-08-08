from http import HTTPStatus

from flask import Flask, jsonify, Response
from webargs.flaskparser import use_kwargs
from validators import country_name_config, track_id_config
from invoice_repositories import get_total_invoice_by_country, get_total_invoice_by_countries
from track_repositories import get_all_info_about_track, get_all_info_about_tracks
from album_repositories import get_time_of_albums

app = Flask(__name__)


@app.route("/")
def index():
    return """
        <a href='/order-price'>Total invoice by countries</a> <hr>
        <a href='/order-price?country_name=USA'>Total invoice by USA</a> <hr>
        <a href='/info-about-track'>Info about all tracks</a> <hr> 
        <a href='/info-about-track?track_id=3'>Info about track 'Fast As a Shark'</a> <hr>
        <a href='/albums-time'>Time of albums</a>
    """


@app.route("/order-price")
@use_kwargs(
    country_name_config,
    location="query"
)
def order_price(country_name=None):
    if country_name is None:
        return jsonify(get_total_invoice_by_countries())

    try:
        result = get_total_invoice_by_country(country_name)
    except ValueError as e:
        return Response(e.__str__(), HTTPStatus.NOT_FOUND)

    return jsonify(result)


@app.route("/info-about-track")
@use_kwargs(
    track_id_config,
    location="query"
)
def info_about_track(track_id=None):
    if track_id is None:
        return jsonify(get_all_info_about_tracks())

    try:
        result = get_all_info_about_track(track_id)
    except ValueError as e:
        return Response(e.__str__(), HTTPStatus.NOT_FOUND)

    return jsonify(result)


@app.route("/albums-time")
def albums_time():
    result = get_time_of_albums()
    return jsonify(result)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)

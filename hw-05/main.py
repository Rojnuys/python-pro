from http import HTTPStatus

from flask import Flask, jsonify, Response
from webargs.flaskparser import use_kwargs
from validators import genre_config
from genre_repositories import get_most_popular_city_by_genre
from geometry import Circle, Point

app = Flask(__name__)


@app.route("/")
def index():
    return """
        <a href='/stats_by_city'>Stats by city without parameter</a> <hr>
        <a href='/stats_by_city?genre=Classical'>Stats by city with correct parameter 'Classical'</a> <hr>
        <a href='/stats_by_city?genre=Alternative'>Stats by city with correct parameter 'Alternative'</a> <hr>
        <a href='/stats_by_city?genre=Science Fiction'>Stats by city with correct parameter 'Science Fiction'</a> <hr>
        <a href='/stats_by_city?genre=Rock And Roll'>Stats by city with correct parameter 'Rock And Roll'</a> <hr>
        <a href='/stats_by_city?genre=Classical234'>Stats by city with wrong parameter 'Classical234'</a> <hr>
        <a href='/point-belongs-to-circle'>The point belongs to the circle</a> <hr>
    """


@app.route("/point-belongs-to-circle")
def point_belongs_to_circle():
    circle = Circle(10, -5, 20)
    point_first = Point(15, -15)
    point_second = Point(31, -5)

    return f"Circle(10, -5, 20): Point(15, -15) - {circle.contains(point_first)}; Point(31, -5): {circle.contains(point_second)}"


@app.route("/stats_by_city")
@use_kwargs(
    genre_config,
    location="query"
)
def stats_by_city(genre):
    if genre is None:
        return Response("The genre parameter is required", HTTPStatus.BAD_REQUEST)

    try:
        result = get_most_popular_city_by_genre(genre)
    except ValueError as e:
        return Response(e.__str__(), HTTPStatus.NOT_FOUND)

    return jsonify(result)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)

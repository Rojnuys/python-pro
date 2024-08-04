from database_handler import execute_query


def get_all_info_about_track(track_id):
    records = execute_query("""
        SELECT *
        FROM tracks
        LEFT JOIN albums ON tracks.AlbumId = albums.AlbumId
        LEFT JOIN media_types ON tracks.MediaTypeId = media_types.MediaTypeId
        LEFT JOIN genres ON tracks.GenreId = genres.GenreId
        WHERE tracks.TrackId = ?;
    """, track_id)

    if not records:
        raise ValueError(f"Don't exist track with id '{track_id}'")

    return records


def get_all_info_about_tracks():
    records = execute_query("""
            SELECT *
            FROM tracks
            LEFT JOIN albums ON tracks.AlbumId = albums.AlbumId
            LEFT JOIN media_types ON tracks.MediaTypeId = media_types.MediaTypeId
            LEFT JOIN genres ON tracks.GenreId = genres.GenreId;
        """)

    return records

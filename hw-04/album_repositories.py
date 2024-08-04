from database_handler import execute_query


def get_time_of_albums():
    records = execute_query("""
        SELECT albums.Title,
               (printf('%02d', SUM(Milliseconds) / 3600000)) || ':' ||
               (printf('%02d', SUM(Milliseconds) % 3600000 / 60000)) || ':' ||
               (printf('%02d', SUM(Milliseconds) % 60000 / 1000)) AS Time
        FROM tracks
        LEFT JOIN albums ON tracks.AlbumId = albums.AlbumId
        GROUP BY albums.Title
    """)

    return records

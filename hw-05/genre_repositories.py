from database_handler import execute_query


def get_most_popular_city_by_genre(genre_name):
    records = execute_query("""
        SELECT City
        FROM (
            SELECT invoices.BillingCity AS City, SUM(Quantity) AS QuantitySum
            FROM invoice_items
            JOIN main.invoices AS invoices ON invoices.InvoiceId = invoice_items.InvoiceId
            JOIN main.tracks AS tracks ON tracks.TrackId = invoice_items.TrackId
            JOIN main.genres AS genres ON genres.GenreId = tracks.GenreId
            WHERE genres.Name = ?
            GROUP BY genres.Name, invoices.BillingCity
            HAVING QuantitySum = (
                SELECT MAX(Quantity)
                FROM (
                    SELECT SUM(Quantity) AS Quantity
                    FROM invoice_items
                    JOIN main.invoices AS invoices ON invoices.InvoiceId = invoice_items.InvoiceId
                    JOIN main.tracks AS tracks ON tracks.TrackId = invoice_items.TrackId
                    JOIN main.genres AS genres ON genres.GenreId = tracks.GenreId
                    WHERE genres.Name = ?
                    GROUP BY genres.Name, invoices.BillingCity
                )
            )
        );
    """, genre_name, genre_name)

    if not records:
        raise ValueError(f"There is no city that listens to the '{genre_name}' genre")

    return records

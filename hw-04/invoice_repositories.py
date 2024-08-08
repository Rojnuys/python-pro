from database_handler import execute_query


def get_total_invoice_by_country(country_name):
    records = execute_query("""
        SELECT invoices.BillingCountry, SUM(UnitPrice * Quantity) AS Sales
        FROM invoice_items
        LEFT JOIN invoices ON invoice_items.InvoiceId = invoices.InvoiceId
        GROUP BY invoices.BillingCountry
        HAVING invoices.BillingCountry = ?;
    """, country_name)

    if not records:
        raise ValueError(f"Don't exist country with name '{country_name}'")

    return records.pop()


def get_total_invoice_by_countries():
    records = execute_query("""
        SELECT invoices.BillingCountry, SUM(UnitPrice * Quantity) AS Sales
        FROM invoice_items
        LEFT JOIN invoices ON invoice_items.InvoiceId = invoices.InvoiceId
        GROUP BY invoices.BillingCountry;
    """)

    return records

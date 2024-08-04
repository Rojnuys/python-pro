from webargs import fields, validate

country_name_config = {
    "country_name": fields.Str(validate=validate.Length(min=2, max=56)),
}

track_id_config = {
    "track_id": fields.Int(validate=validate.Range(min=1)),
}
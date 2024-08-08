from webargs import fields, validate

genre_config = {
    "genre": fields.Str(load_default=None, validate=validate.Length(min=2, max=255)),
}
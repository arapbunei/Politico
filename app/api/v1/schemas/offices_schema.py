from marshmallow import Schema, fields, post_dump
from ..utils.validator import required

class OfficeSchema(Schema):

    """ schema for office object """

    id = fields.Int(dump_only=True)
    type = fields.Str(required=False, validate=(required))
    name = fields.Str(required=True, validate=(required))
   




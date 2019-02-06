from marshmallow import Schema, fields, post_dump
from ..utils.validator import required



class PartySchema(Schema):
    """ Class to validate schema for Meetup object """

    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=(required))
    hqaddress = fields.Str(required=True, validate=(required))
    logourl = fields.Str(required=True, validate=(required))
   



    



    

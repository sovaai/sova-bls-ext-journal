from tortoise.models import Model
from tortoise import fields


class JournalModel(Model):
    """

    """
    inf = fields.IntField()
    chat = fields.IntField()
    req_ts = fields.DatetimeField()
    request = fields.TextField()
    resp_ts = fields.DatetimeField()
    response = fields.TextField()
    req_cntx = fields.JSONField()
    resp_cntx = fields.JSONField()
    is_event = fields.BooleanField()
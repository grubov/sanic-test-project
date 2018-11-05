from marshmallow import Schema, fields


class ContractSchema(Schema):
    title = fields.String(required=True)
    price = fields.Float()
    comment = fields.String()


class PaymentSchema(Schema):
    id = fields.Integer()
    contracts_id = fields.Integer()
    amount = fields.Float()

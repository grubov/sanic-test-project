from marshmallow import Schema, fields


class ContractSchema(Schema):
    title = fields.String(required=True)
    price = fields.Float(required=True)
    comment = fields.String()


class PaymentSchema(Schema):
    contracts_id = fields.Integer(required=True)
    amount = fields.Float(required=True)

from sqlalchemy.sql import select

from service_api.models import Payments
from service_api.database import engine


async def get_payment_by_id(payment_id):
    query = select([Payments]).where(Payments.c.id == payment_id)
    conn = engine.connect()
    result = conn.execute(query)
    return dict(result.fetchone())


async def delete_payment_by_id(payment_id):
    query = Payments.delete().where(Payments.c.id == payment_id)
    conn = engine.connect()
    result = conn.execute(query)
    return {'DELETE': 'OK'}


async def get_all_payments_for_current_contract(contract_id):
    """Get all contracts from database"""
    query = select([Payments]).where(Payments.c.contracts_id == contract_id)
    conn = engine.connect()
    result = conn.execute(query).fetchall()
    res = []
    for i in result:
        res.append(dict(i))
    return res


async def post_new_payment(json_data):
    """Add new payment to database"""
    query = Payments.insert()
    conn = engine.connect()
    result = conn.execute(query, json_data)
    payment_id = result.inserted_primary_key.pop()
    return payment_id

from sanic.exceptions import abort
from sqlalchemy.sql import select, and_

from service_api.models import Payments
from service_api.database import engine


async def get_payment_by_id(contract_id, payment_id):
    """Get payment by id from database"""
    query = select([Payments]).where(
                                    and_(
                                        Payments.c.id == payment_id,
                                        Payments.c.contracts_id == contract_id
                                    )
                                )
    conn = engine.connect()
    result = conn.execute(query).fetchone()
    if result:
        return dict(result)
    else:
        return abort(404)


async def delete_payment_by_id(contract_id, payment_id):
    """Delete payment by id from database"""
    payment = await get_payment_by_id(contract_id, payment_id)
    query = Payments.delete().where(
                                    and_(
                                        Payments.c.id == payment_id,
                                        Payments.c.contracts_id == contract_id
                                    )
                                )
    conn = engine.connect()
    conn.execute(query)
    return payment


async def get_all_payments_for_current_contract(contract_id):
    """Get all payments from database for current contract"""
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

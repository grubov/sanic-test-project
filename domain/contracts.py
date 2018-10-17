from sqlalchemy.sql import select

from service_api.models import Contracts, engine


async def get_contract_by_id(contract_id):
    stmt = select([Contracts]).where(Contracts.c.id == contract_id)
    conn = engine.connect()
    result = conn.execute(stmt)
    return dict(result.fetchone())

#
# @app.route('/<contract_id:int>', methods=['GET'])
# async def get_contract(request, contract_id):
#     """Get the contract from database with current contract_id"""
#     s = select([contracts]).where(contracts.c.id == contract_id)
#     conn = engine.connect()
#     result = conn.execute(s)
# return response.json({result})
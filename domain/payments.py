# from sqlalchemy.sql import select
# import json
#
# from service_api.models import Contracts, Payments
# from service_api.database import engine
#
#
# async def get_payment_by_id(contract_id):
#     stmt = select([Contracts]).where(Contracts.c.id == contract_id)
#     conn = engine.connect()
#     result = conn.execute(stmt)
#     return dict(result.fetchone())
#
#
# async def put_payment_by_id(request, contract_id):
#     json_data = request.json
#     u = Contracts.update().where(Contracts.c.id == contract_id)
#     conn = engine.connect()
#     result = conn.execute(u, json_data)
#     return {'PUT': 'OK'}
#
#
# async def delete_payment_by_id(contract_id):
#     d = Contracts.delete().where(Contracts.c.id == contract_id)
#     conn = engine.connect()
#     result = conn.execute(d)
#     return {'DELETE': 'OK'}
#
#
# async def get_all_payments():
#     """Get all contracts from database"""
#     s = select([Contracts])
#     conn = engine.connect()
#     result = conn.execute(s).fetchall()
#     res=[]
#     for i in result:
#         res.append(dict(i))
#     return res
#
#
# async def post_new_payment(request):
#     """Post new contract to database"""
#     ins = Payments.insert()
#     json_data = request.json
#     conn = engine.connect()
#     result = conn.execute(ins, json_data)
#     return {'POST': f'ADDED WITH ID={result.inserted_primary_key}'}

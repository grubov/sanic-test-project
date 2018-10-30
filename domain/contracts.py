from sqlalchemy.sql import select

from service_api.models import Contracts
# from service_api.database import engine
from aiopg.sa import create_engine

dsn = 'dbname=postgres user=postgres password=postgres host=127.0.0.1'


async def get_contract_by_id(contract_id):
    async with create_engine(dsn) as engine:
        async with engine.acquire() as conn:
            stmt = select([Contracts]).where(Contracts.c.id == contract_id)
            result = await conn.execute(stmt)
            d = {}
            # for rowproxy in result:
            #     d = dict(rowproxy.items())
            a = [i.items() for i in result]
            return a


async def put_contract_by_id(request, contract_id):
    json_data = request.json
    u = Contracts.update().where(Contracts.c.id == contract_id)
    conn = engine.connect()
    result = conn.execute(u, json_data)
    return {'PUT': 'OK'}


async def delete_contract_by_id(contract_id):
    d = Contracts.delete().where(Contracts.c.id == contract_id)
    conn = engine.connect()
    result = conn.execute(d)
    return {'DELETE': 'OK'}


async def get_all_contracts():
    """Get all contracts from database"""
    s = select([Contracts])
    conn = engine.connect()
    result = conn.execute(s).fetchall()
    res = []
    for i in result:
        res.append(dict(i))
    return res


async def post_new_contract(request):
    """Post new contract to database"""
    ins = Contracts.insert()
    json_data = request.json
    conn = engine.connect()
    result = conn.execute(ins, json_data)
    return {'POST': f'ADDED WITH ID={result.inserted_primary_key}'}

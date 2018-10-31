from sqlalchemy.sql import select
from aiopg.sa import create_engine
from service_api.database import engine
from service_api.models import Contracts

dsn = 'dbname=postgres user=postgres password=postgres host=127.0.0.1'


async def get_contract_by_id(contract_id):
    """Get all contracts from database"""
    async with create_engine(dsn) as engine_aiopg:
        async with engine_aiopg.acquire() as conn:
            stmt = select([Contracts]).where(Contracts.c.id == contract_id)
            result = await conn.execute(stmt)
            d = {}
            for rowproxy in result:
                d = dict(rowproxy.items())
            return d


async def put_contract_by_id(json_data, contract_id):
    """Change contract by id in database"""
    u = Contracts.update().where(Contracts.c.id == contract_id)
    conn = engine.connect()
    conn.execute(u, json_data)
    return json_data


async def delete_contract_by_id(contract_id):
    """Delete contract by id from database"""
    d = Contracts.delete().where(Contracts.c.id == contract_id)
    conn = engine.connect()
    conn.execute(d)
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


async def post_new_contract(json_data):
    """Post new contract to database"""
    ins = Contracts.insert()
    conn = engine.connect()
    result = conn.execute(ins, json_data)
    id = result.inserted_primary_key.pop()
    # return {'id': id}
    return id

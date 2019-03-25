from sqlalchemy.sql import select, update
from aiopg.sa import create_engine

from service_api.database import engine
from service_api.models import Contracts
from service_api.database import DSN


async def get_contract_by_id(contract_id):
    """Get contract by id from database"""
    async with create_engine(DSN) as engine_aiopg:
        async with engine_aiopg.acquire() as conn:
            query = select([Contracts]).where(Contracts.c.id == contract_id)
            result = await conn.execute(query)
            contract = {}
            for rowproxy in result:
                contract = dict(rowproxy.items())
            return contract


async def put_contract_by_id(json_data, contract_id):
    """Change contract by id in database"""
    async with create_engine(DSN) as engine_aiopg:
        async with engine_aiopg.acquire() as conn:
            query = update(Contracts).where(Contracts.c.id == contract_id).values(**json_data)
            await conn.execute(query)
            contract = await get_contract_by_id(contract_id)
            return contract


async def delete_contract_by_id(contract_id):
    """Delete contract by id from database"""
    async with create_engine(DSN) as engine_aiopg:
        async with engine_aiopg.acquire() as conn:
            contract = await get_contract_by_id(contract_id)
            query = Contracts.delete().where(Contracts.c.id == contract_id)
            await conn.execute(query)
            return contract


async def get_all_contracts():
    """Get all contracts from database"""
    async with create_engine(DSN) as engine_aiopg:
        async with engine_aiopg.acquire() as conn:
            query = select([Contracts])
            result = await conn.execute(query)
            result_list = []
            for i in result:
                result_list.append(dict(i))
            return result_list


async def post_new_contract(json_data):
    """Add new contract to database"""
    async with create_engine(DSN) as engine_aiopg:
        async with engine_aiopg.acquire() as conn:
            query = Contracts.insert().values(**json_data)
            result = await conn.execute(query, json_data)
            contract_id = None
            async for row in result:
                contract_id = row['id']
            return contract_id

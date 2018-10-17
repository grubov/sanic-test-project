from sanic import response

from domain.contracts import get_contract_by_id
from resources import BaseResource


class ContractResource(BaseResource):
    async def get(self, request, contract_id):
        contract = await get_contract_by_id(contract_id)
        return response.json(contract)

    async def post(self):
        pass

    async def put(self):
        pass

    async def delete(self):
        pass


class ContractsResource(BaseResource):
    async def get(self):
        pass

    async def post(self):
        pass

    async def put(self):
        pass
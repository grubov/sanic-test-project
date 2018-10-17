from sanic import response

from domain.contracts import get_contract_by_id, put_contract_by_id, delete_contract_by_id
from resources import BaseResource


class ContractResource(BaseResource):
    async def get(self, request, contract_id):
        contract = await get_contract_by_id(contract_id)
        return response.json(contract)

    async def post(self, request):
        pass

    async def put(self, request, contract_id):
        contract = await put_contract_by_id(request, contract_id)
        return response.json(contract)

    async def delete(self, request, contract_id):
        contract = await delete_contract_by_id(contract_id)
        return response.json(contract)


class ContractsResource(BaseResource):
    async def get(self, request):
        pass

    async def post(self, request):
        pass

    async def put(self, request):
        pass
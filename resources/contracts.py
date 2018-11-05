from sanic import response
from marshmallow import ValidationError

from resources import BaseResource
from domain.contracts import get_contract_by_id, put_contract_by_id, delete_contract_by_id
from domain.contracts import get_all_contracts, post_new_contract
from service_api.services.schemas import ContractSchema


class ContractResource(BaseResource):
    async def get(self, request, contract_id):
        contract = await get_contract_by_id(contract_id)
        return response.json(contract)

    async def put(self, request, contract_id):
        data, err = ContractSchema().load(request.json)
        if err:
            raise ValidationError("ValidationError")
        contract = await put_contract_by_id(data, contract_id)
        return response.json(contract)

    async def delete(self, request, contract_id):
        contract = await delete_contract_by_id(contract_id)
        return response.json(contract)


class ContractsResource(BaseResource):
    async def get(self, request):
        contracts = await get_all_contracts()
        return response.json(contracts)

    async def post(self, request):
        data, err = ContractSchema().load(request.json)
        if err:
            raise ValidationError("ValidationError")
        contract_id = await post_new_contract(data)
        contract = await get_contract_by_id(contract_id)
        return response.json(contract)

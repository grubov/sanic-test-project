from sanic import response
from marshmallow import ValidationError

from domain.contracts import get_contract_by_id, put_contract_by_id, delete_contract_by_id
from domain.contracts import get_all_contracts, post_new_contract
from resources import BaseResource
from service_api.services.schemas import ContractSchema, PaymentSchema, ContractIdListSchema


class ContractResource(BaseResource):
    async def get(self, request, contract_id):
        contract = await get_contract_by_id(contract_id)
        return response.json(contract)

    async def put(self, request, contract_id):
        json_data = request.json
        contract = await put_contract_by_id(json_data, contract_id)
        return response.json(contract)

    async def delete(self, request, contract_id):
        contract = await delete_contract_by_id(contract_id)
        return response.json(contract)


class ContractsResource(BaseResource):
    async def get(self, request):
        contracts = await get_all_contracts()
        return response.json(contracts)

    async def post(self, request):
        json_data = request.json
        data = ContractSchema().validate(json_data)
        if data:
            raise ValidationError("Error")
        json_data = request.json
        contract_id = await post_new_contract(json_data)
        contract = await get_contract_by_id(contract_id)
        return response.json(contract)


class PaymentResource(BaseResource):
    async def get(self, request):
        contracts = await get_all_contracts()
        return response.json(contracts)

    async def post(self, request):
        pass

    async def put(self, request):
        pass


class SmokeResource(BaseResource):
    async def get(self, request):
        """Simple test"""
        return response.json({"message": "OK"})

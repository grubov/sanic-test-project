from sanic import response

from domain.contracts import get_contract_by_id, put_contract_by_id, delete_contract_by_id
from domain.contracts import get_all_contracts, post_new_contract
from resources import BaseResource


from marshmallow import ValidationError
from service_api.services.schemas import (ContractSchema, PaymentSchema, ContractIdListSchema)


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
        contracts = await get_all_contracts()
        return response.json(contracts)

    async def post(self, request):
        json_data = request.json
        try:
            mresult, errors = ContractSchema().load(json_data)
        except ValidationError as err:
            return response.json({"error": "err.messages"})
        contracts = await post_new_contract(request)
        return response.json(contracts)

    async def put(self, request):
        pass


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

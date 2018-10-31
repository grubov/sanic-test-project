from sanic import response
from sanic.exceptions import InvalidUsage

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
        # try:
        #     json_data = request.json
        #     data, errors = ContractSchema(strict=True).validate(json_data)
        # except ValidationError as err:
        #     return response.json({"error": err.messages}, 400)
        # except InvalidUsage as err:
        #     return response.json({"error": "Invalid JSON"}, 400)
        json_data = request.json
        contract_id = await post_new_contract(json_data)
        contract = await get_contract_by_id(contract_id)
        return response.json(contract)

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

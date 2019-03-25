from sanic import response
from marshmallow import ValidationError

from resources import BaseResource
from domain.contracts import get_contract_by_id, put_contract_by_id, delete_contract_by_id
from domain.contracts import get_all_contracts, post_new_contract
from service_api.services.schemas import ContractSchema
from service_api.kafka_producer import producer


class ContractResource(BaseResource):
    async def get(self, request, contract_id):
        """Get contract by id from database"""
        contract = await get_contract_by_id(contract_id)
        producer.send('sanic', b'Operation: Get contract by id. Success: True')
        return response.json(contract)

    async def put(self, request, contract_id):
        """Change contract by id in database"""
        data, err = ContractSchema().load(request.json)
        if err:
            raise ValidationError('ValidationError')
        contract = await put_contract_by_id(data, contract_id)
        producer.send('sanic', b'Operation: Change contract by id. Success: True')
        return response.json(contract)

    async def delete(self, request, contract_id):
        """Delete contract by id from database"""
        contract = await delete_contract_by_id(contract_id)
        producer.send('sanic', b'Operation: Delete contract by id. Success: True')
        return response.json(contract)


class ContractsResource(BaseResource):
    async def get(self, request):
        """Get all contracts from database"""
        contracts = await get_all_contracts()
        producer.send('sanic', b'Operation: Get all contracts. Success: True')
        return response.json(contracts)

    async def post(self, request):
        """Add new contract to database"""
        data, err = ContractSchema().load(request.json)
        if err:
            raise ValidationError('ValidationError')
        contract_id = await post_new_contract(data)
        contract = await get_contract_by_id(contract_id)
        producer.send('sanic', b'Operation: Add new contract. Success: True')
        return response.json(contract)

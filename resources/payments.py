from sanic import response
from marshmallow import ValidationError

from resources import BaseResource
from domain.payments import get_payment_by_id, delete_payment_by_id
from domain.payments import get_all_payments_for_current_contract, post_new_payment
from service_api.services.schemas import PaymentSchema
from service_api.kafka_producer import producer


class PaymentResource(BaseResource):
    async def get(self, request, contract_id, payment_id):
        """Get payment by id from database"""
        payment = await get_payment_by_id(contract_id, payment_id)
        producer.send('sanic', b'Operation: Get payment by id. Success: True')
        return response.json(payment)

    async def delete(self, request, contract_id, payment_id):
        """Delete payment by id in database"""
        payment = await delete_payment_by_id(contract_id, payment_id)
        producer.send('sanic', b'Operation: Delete payment by id. Success: True')
        return response.json(payment)


class PaymentsResource(BaseResource):
    async def get(self, request, contract_id):
        """Get all payments from database for current contract"""
        payments = await get_all_payments_for_current_contract(contract_id)
        producer.send('sanic', b'Operation: Get all payments for current contract. Success: True')
        return response.json(payments)

    async def post(self, request, contract_id):
        """Add new payment to database"""
        data, err = PaymentSchema().load(request.json)
        if err:
            raise ValidationError('ValidationError')
        data['contracts_id'] = contract_id
        payment_id = await post_new_payment(data)
        payment = await get_payment_by_id(contract_id, payment_id)
        producer.send('sanic', b'Operation: Add new payment. Success: True')
        return response.json(payment)

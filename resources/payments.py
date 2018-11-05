from sanic import response
from marshmallow import ValidationError

from resources import BaseResource
from domain.payments import get_payment_by_id, delete_payment_by_id
from domain.payments import get_all_payments_for_current_contract, post_new_payment
from service_api.services.schemas import PaymentSchema


class PaymentResource(BaseResource):
    async def get(self, request, payment_id):
        payment = await get_payment_by_id(payment_id)
        return response.json(payment)

    async def delete(self, request, payment_id):
        payment = await delete_payment_by_id(payment_id)
        return response.json(payment)


class PaymentsResource(BaseResource):
    async def get(self, request, contract_id):
        payments = await get_all_payments_for_current_contract(contract_id)
        return response.json(payments)

    async def post(self, request, contract_id):
        data, err = PaymentSchema().load(request.json)
        if err:
            raise ValidationError("ValidationError")
        data['contracts_id'] = contract_id
        payment_id = await post_new_payment(data)
        payment = await get_payment_by_id(payment_id)
        return response.json(payment)

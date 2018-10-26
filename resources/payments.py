from sanic import response

from domain.payments import get_payment_by_id, delete_payment_by_id
from domain.payments import get_all_payments_for_current_contract, post_new_payment
from resources import BaseResource


class PaymentResource(BaseResource):
    async def get(self, request, payment_id):
        payment = await get_payment_by_id(payment_id)
        return response.json(payment)

    async def delete(self, request, payment_id):
        payment = await delete_payment_by_id(payment_id)
        return response.json(payment)


class PaymentsResource(BaseResource):
    async def get(self, request, contract_id):
        contracts = await get_all_payments_for_current_contract(contract_id)
        return response.json(contracts)

    async def post(self, request, contract_id):
        contracts = await post_new_payment(request)
        return response.json(contracts)

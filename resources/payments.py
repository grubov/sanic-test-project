# from sanic import response
#
# from domain.payments import get_payment_by_id, put_payment_by_id, delete_payment_by_id
# from resources import BaseResource
#
#
# class PaymentResource(BaseResource):
#     async def get(self, request, payment_id):
#         payment = await get_payment_by_id(payment_id)
#         return response.json(payment)
#
#     async def post(self, request):
#         pass
#
#     async def put(self, request, payment_id):
#         payment = await put_payment_by_id(request, payment_id)
#         return response.json(payment)
#
#     async def delete(self, request, payment_id):
#         payment = await delete_payment_by_id(payment_id)
#         return response.json(payment)

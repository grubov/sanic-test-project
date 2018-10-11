from sanic import Sanic
from sanic import response
from sqlalchemy.sql import select
from models import contracts, payments, engine
app = Sanic()


@app.route('/', methods=['GET'])
async def get_contracts(request):
    s = select([contracts])
    conn = engine.connect()
    result = conn.execute(s)
    return response.json({result})

#
# @app.route('/', methods=['POST'])
# async def post_contract(request):
#     ins = select([contracts])
#     conn = engine.connect()
#     result = conn.execute(ins)
#     return response.json({"POST": request.json})


@app.route('/', methods=['POST'])
async def post_contract(request):
    ins = select([contracts])
    conn = engine.connect()
    title = request.json.get('title')
    price = request.json.get('price')
    comment = request.json.get('comment')
    user =

    result = conn.execute(ins)
    return response.json({"POST": title})


@app.route('/<contract_id:int>', methods=['GET'])
async def get_contract(request, contract_id):
    s = select([contracts]).where(contracts.c.id == contract_id)
    conn = engine.connect()
    result = conn.execute(s)
    return response.json({result})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

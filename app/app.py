from sanic import Sanic
from sanic import response
from sqlalchemy import update
from sqlalchemy.sql import select
from models import contracts, payments, engine
app = Sanic()


@app.route('/', methods=['GET'])
async def get_contracts(request):
    s = select([contracts])
    conn = engine.connect()
    result = conn.execute(s)
    return response.json({result})


@app.route('/', methods=['POST'])
async def post_contract(request):
    conn = engine.connect()

    # title = request.json.get('title')
    # price = request.json.get('price')
    # comment = request.json.get('comment')

    ins = contracts.insert()
    json_data = request.json

    # cont = {
    #     'title': title,
    #     'price': price,
    #     'comment': comment
    # }

    result = conn.execute(ins, json_data)
    return response.json({'POST': f'CONTRACT ADDED TO DATABASE WITH ID={result.inserted_primary_key}'})


@app.route('/<contract_id:int>', methods=['GET'])
async def get_contract(request, contract_id):
    s = select([contracts]).where(contracts.c.id == contract_id)
    conn = engine.connect()
    result = conn.execute(s)
    return response.json({result})


@app.route('/<contract_id:int>', methods=['PUT'])
async def put_contract(request, contract_id):
    json_data = request.json
    u = contracts.update().where(contracts.c.id == contract_id)
    conn = engine.connect()
    result = conn.execute(u, json_data)
    return response.json({'POST': f'CONTRACT UPDATED IN DATABASE WITH ID={contract_id}'})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

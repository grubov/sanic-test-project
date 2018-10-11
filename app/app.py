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


@app.route('/', methods=['POST'])
async def post_contract(request):
    conn = engine.connect()

    # title = request.json.get('title')
    # price = request.json.get('price')
    # comment = request.json.get('comment')

    ins = contracts.insert()
    cont = request.json

    # cont = {
    #     'title': title,
    #     'price': price,
    #     'comment': comment
    # }

    result = conn.execute(ins, cont)
    return response.json({'POST': f'CONTRACT ADDED TO DATABASE WITH ID={result.inserted_primary_key}'})


@app.route('/<contract_id:int>', methods=['GET'])
async def get_contract(request, contract_id):
    s = select([contracts]).where(contracts.c.id == contract_id)
    conn = engine.connect()
    result = conn.execute(s)
    return response.json({result})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

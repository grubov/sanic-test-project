from service_api.app import app
import aiohttp


async def async_test_smoke():
    """
    GET request
    """
    resp = await app.test_cli.get('/contracts/v1/smoke')
    assert resp.status == 200
    resp_json = await resp.json()
    assert resp_json == {"message": "OK"}

def test_smoke():
    """Start with a blank database."""
    request, response = app.test_client.get('/contracts/v1/smoke')
    assert response.json.get("message") == "OK"


def test_contracts_returns_200():
    request, response = app.test_client.get('/contracts/v1/contracts/')
    assert response.status == 200


def test_not_found_error():
    request, response = app.test_client.get('/')
    assert response.status == 404


def test_get_contract():
    data = {
        "id": 7,
        "title": "A1",
        "price": 100,
        "comment": "Contract 117",
        "expiration_date": 1516233600
    }
    request, response = app.test_client.get('/contracts/v1/contracts/7')
    assert response.json == data


def test_get_id_of_contract():
    request, response = app.test_client.get('/contracts/v1/contracts/6')
    assert response.json.get('id') == 6

from sanic import Blueprint, Sanic

from resources.contracts import ContractResource, ContractsResource
from service_api.constants import SERVICE_NAME


def load_api(app: Sanic):
    api_v1 = Blueprint('v1', url_prefix=f'/{SERVICE_NAME}/v1', strict_slashes=False)

    api_v1.add_route(ContractResource.as_view(), "/contracts/<contract_id:int>", strict_slashes=False)
    api_v1.add_route(ContractsResource.as_view(), "/contracts/", strict_slashes=False)

    app.blueprint(api_v1)

from sqlalchemy import create_engine
from service_api.models import metadata, Contracts, Payments

engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres', echo=True)
URI = 'dbname=postgres user=postgres password=postgres host=127.0.0.1'


def create_all():
    metadata.create_all(engine)


def drop_all():
    metadata.drop_all(engine)


def populate():
    ins_test_contract = Contracts.insert().values(title='A1', price='100.00', comment='Contract 1')
    ins_test_payment = Payments.insert().values(contracts_id='1', amount='22.00')
    ins_test_payment_2 = Payments.insert().values(contracts_id='1', amount='33.00')
    print(str(ins_test_contract))
    print(str(ins_test_payment))
    conn = engine.connect()
    conn.execute(ins_test_contract)
    conn.execute(ins_test_payment)
    conn.execute(ins_test_payment_2)

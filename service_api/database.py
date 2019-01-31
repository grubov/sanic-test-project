import os
from sqlalchemy import create_engine
from service_api.models import metadata, Contracts, Payments

SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/postgres'
# SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')

engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
DSN = SQLALCHEMY_DATABASE_URI


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

from sqlalchemy import create_engine
from service_api.models import metadata

engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres', echo=True)
# metadata.drop_all(engine)
metadata.create_all(engine)

# ins = contracts.insert().values(title='A1', price='100.00', comment='Contract 1')
# # ins2 = payments.insert().values(contracts_id='2', amount='22.00', date='2018-01-18')
#
#
# conn = engine.connect()
# result = conn.execute(ins)

# print(str(ins))

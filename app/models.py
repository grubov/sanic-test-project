from sqlalchemy import Table, Column, Integer, Float, String, MetaData, Date, ForeignKey, \
    create_engine
from datetime import date

metadata = MetaData()

contracts = Table('contracts', metadata,
                  Column('id', Integer, primary_key=True, autoincrement=True),
                  Column('title', String, nullable=False),
                  Column('price', Float),
                  Column('comment', String),
                  Column('expiration_date', Date(), default=date.today)
                  )

payments = Table('payments', metadata,
                 Column('id', Integer, primary_key=True, autoincrement=True),
                 Column('contracts_id', None, ForeignKey('contracts.id')),
                 Column('amount', Float),
                 Column('date', Date(), default=date.today)
                 )


engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres', echo=True)
# metadata.drop_all(engine)
metadata.create_all(engine)

ins = contracts.insert().values(title='A1', price='100.00', comment='Contract 1')
# ins2 = payments.insert().values(contracts_id='2', amount='22.00', date='2018-01-18')


conn = engine.connect()
result = conn.execute(ins)

# print(str(ins))

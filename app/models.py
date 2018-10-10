from sqlalchemy import Table, Column, Integer, Float, String, MetaData, DateTime, ForeignKey, \
    create_engine

metadata = MetaData()

contracts = Table('contracts', metadata,
                  Column('id', Integer, primary_key=True, autoincrement=True),
                  Column('title', String, nullable=False),
                  Column('price', Float),
                  Column('comment', String),
                  Column('expiration_date', DateTime)
                  )

payments = Table('payments', metadata,
                 Column('id', Integer, primary_key=True, autoincrement=True),
                 Column('contracts_id', None, ForeignKey('contracts.id')),
                 Column('amount', Float),
                 Column('date', DateTime)
                 )


engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres', echo=True)
metadata.create_all(engine)

ins = contracts.insert().values(title='A1', price='100.00', comment='Contract 1')

conn = engine.connect()
result = conn.execute(ins)

print(str(ins))

from sqlalchemy import Table, Column, Integer, Float, String, MetaData, Date, ForeignKey
from datetime import date

metadata = MetaData()

Contracts = Table(
    'contracts',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('title', String, nullable=False),
    Column('price', Float),
    Column('comment', String),
    Column('expiration_date', Date, default=date.today)
)

Payments = Table(
    'payments',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('contracts_id', None, ForeignKey('contracts.id')),
    Column('amount', Float),
    Column('date', Date, default=date.today)
)

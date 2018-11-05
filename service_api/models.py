from sqlalchemy import Table, MetaData, Column, ForeignKey, Integer, Float, String, Date, DateTime
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
    Column('date_time', DateTime, default=date.today)
)

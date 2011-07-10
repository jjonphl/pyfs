from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import mapper
from ewb.finstudio.fs import get_metadata

__all__ = ['Entity', 'Customer']

metadata = get_metadata()

entity = Table('t_entity', metadata, autoload=True, include_columns=[
    'entity', 'description', 'calendar', 'account_category', 
    'prev_cob_date', 'cob_date', 'next_cob_date', 'current_year',
    'current_period', 'reporting_year', 'reporting_period', 
    'lcl_currency', 'rpt_currency'])

customer = Table('t_customer', metadata, autoload=True, include_columns=[
    'customer_nr', 'start_validity_date', 'end_validity_date',
    'customer_shortname', 'is_parent_ind', 'account_officer', 
    'nationality', 'domicile', 'intercompany', 'industry_code',
    'customer_type', 'economic_sector', 'global_customer', 'nace_code',
    'customer_attribute1'])


class Entity(object):
    pass

class Customer(object):
    pass

mapper(Entity, entity)
mapper(Customer, customer)

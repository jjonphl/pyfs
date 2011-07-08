from sqlalchemy import Table, Column, Integer, String

__all__ = ['']

metadata = get_metadata()

entity = Table('t_entity', metadata, autoload=True, include_columns=[
    'entity', 'description', 'calendar', 'account_category', 
    'prev_cob_date', 'cob_date', 'next_cob_date', 'current_year',
    'current_period', 'reporting_year', 'reporting_period', 
    'lcl_currency', 'rpt_currency'])

def get_schema

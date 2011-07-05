import ewbc.finstudio as fs

con = fs.Connection('172.28.10.60', 'fibdbo', 'fibdbo')


con.entities   # return entities
rbu = con.entities['EW-RBU']

# market data
con.market.exchange_rates['PDS-WAR']
con.market.rates['TPR']
con.market.securities 

# static data
con.static.customers
con.static.currencies
con.static.deal_types
con.static.deal_subtypes

# calendar data
con.calendars['Calendar1']

# entity top-level
rbu.cob_date
rbu.current_period
rbu.reporting_period


# entity profit centre module
rbu.profit_centres
pc001 = rbu.profit_centres['1']


# entity GL module
rbu.chart_of_accounts
rbu.chart_of_accounts['2000000'].balance()

# entity transactions module
rbu.loans['deal_id']
rbu.loans.active      # collection of active loans




# queries to answer
# group by having balance > 0 ?

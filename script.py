from pytiingo.rest.client import Client

c = Client('57dcb3efa474a3f7d95b0bdccd7e6d274333724e')

c.eod.get_prices('tsla')

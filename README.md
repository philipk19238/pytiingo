# Pytiingo
Pytiingo is a Python SDK written for the Tiingo Financial Markets API. Tiingo delivers performant access to data from financial markets such as equities, cyrptocurrencies, and forex. They also support queryable fundamentals and news data spanning 20+ years. 

Use Pytiingo to query Tiingo's REST endpoints and receive data in JSON or Pandas format. Pytiingo will support real time streaming of financial data in the coming future. This library requires a free API key, which can be retrieved by making a free account on their <a href="https://api.tiingo.com/">website</a>. You can also look at all the available functionality in their <a href="https://api.tiingo.com/documentation/general/overview">API Documentation</a>.

## Install 
Install the latest package using pip: 
```shell
pip install pytiingo
```
To install from the source, clone the directory using: 
```shell
git clone git@github.com:philipk19238/pytiingo.git
```
Navigate to the project directory and run: 
```
python setup.py --install
```

## REST Usage
Documentation below interfaces with Tiingo's REST endpoints

## Initialize the Client 
The REST Client can be initialized as follows: 
```python 
from pytiingo import RESTClient 

client = RESTClient(token='YOUR_API_TOKEN') 
```
If you want your data in a Pandas format, use: 
```python 
from pytiingo import RESTClient 

client = RESTClient(token='YOUR_API_TOKEN', output_format='pandas') 
```

## Sample API Calls 

### EOD Equities 
```python 
from pytiingo import RESTClient 

client = RESTClient(token='YOUR_API_TOKEN') 
price = client.eod.get_prices('GOOG')
```

### Cryptocurrencies 
```python 
from pytiingo import RESTClient

client = RESTClient(token='YOUR_API_TOKEN')
prices = client.crypto.get_prices(tickers='BTCUSD',
                                  startDate='2019-01-02',
                                  resampleFreq='5min')
```
### Forex
```python
from pytiingo import RESTClient

client = RESTClient(token='YOUR_API_TOKEN')
prices = client.forex.get_prices('AUDUSD')
```
### Real Time Equities
```python
from pytiingo import RESTClient

client = RESTClient(token='YOUR_API_TOKEN')
prices = client.iex.get_prices('GOOG')
```

### Fundamentals 
```python
from pytiingo import RESTClient

client = RESTClient(token='YOUR_API_TOKEN')
metrics = client.fundamentals.get_daily_metrics('GOOG')
```

### News 
```python
from pytiingo import RESTClient

client = RESTClient(token='YOUR_API_TOKEN')
news = client.news.get_news(tickers=['AAPL', 'GOOG'],
                            tags=['election', 'argentina'])
```

## Contributing
All contributors are welcome! Just make a pull request :)

## TODOS: 
* Finish WebsocketClient for data streaming
* Add Unit Tests 
* Integrate CI Pipeline 
* Add Integration Tests







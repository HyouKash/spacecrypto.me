from datetime import datetime
from influxdb import InfluxDBClient
from websocket import create_connection
from datetime import datetime
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import time
import json

token = "CI8YH1fun60_u4c6Xzk941Od6q2ZaM4qGv9_5olry2oYoUk0Uj8rpo-OSXWgimO6KM7AGRot9wrUpvTTBjjcoA=="
org = "my-org"
bucket = "Crypto"


def func_logPrice(coin, price, kind):
    client = InfluxDBClient(url="http://139.59.147.33:8086", token=token, org=org)
    point = Point("BTC") \
        .field("Price", price) \
        .time(datetime.utcnow(), WritePrecision.NS)

    write_api = client.write_api(write_options=SYNCHRONOUS)

    write_api.write(bucket, org, point)


options = {'origin': 'https://exchange.blockchain.com'}
url = "wss://ws.blockchain.info/mercury-gateway/v1/ws"

ws = create_connection(url, **options)

msg = '{"action": "subscribe", "channel": "ticker", "symbol": "BTC-USD"}'
ws.send(msg)
ws.recv()

while True:
    try:
        data = json.loads(ws.recv())
        func_logPrice("BTC", data["mark_price"], "BTC-USD")
    except:
        pass
    time.sleep(60)

ws.close()


import subprocess
import time
import threading
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from datetime import datetime

token = "CI8YH1fun60_u4c6Xzk941Od6q2ZaM4qGv9_5olry2oYoUk0Uj8rpo-OSXWgimO6KM7AGRot9wrUpvTTBjjcoA=="
org = "my-org"
bucket = "Crypto"


def getblockcount():
    subproces = subprocess.Popen("bitcoin-cli getblockcount", shell=True, stdout=subprocess.PIPE)

    output = subproces.stdout.read().decode().strip()

    print(output)

    client = InfluxDBClient(url="http://localhost:8086", token=token, org=org)
    point = Point("BTC") \
        .field("BlockCount", int(output)) \
        .time(datetime.utcnow(), WritePrecision.NS)

    write_api = client.write_api(write_options=SYNCHRONOUS)

    write_api.write(bucket, org, point)


def getdifficulty():
    subproces = subprocess.Popen("bitcoin-cli getdifficulty", shell=True, stdout=subprocess.PIPE)

    output = subproces.stdout.read().decode().strip()

    print(output)

    client = InfluxDBClient(url="http://localhost:8086", token=token, org=org)
    point = Point("BTC") \
        .field("Difficulty", int(output.split(".")[0])) \
        .time(datetime.utcnow(), WritePrecision.NS)

    write_api = client.write_api(write_options=SYNCHRONOUS)

    write_api.write(bucket, org, point)


def getunconfirmedtx():
    subproces = subprocess.Popen('bitcoin-cli getmininginfo | jq -r ".pooledtx"', shell=True, stdout=subprocess.PIPE)

    output = subproces.stdout.read().decode().strip()

    print(output)

    client = InfluxDBClient(url="http://localhost:8086", token=token, org=org)
    point = Point("BTC") \
        .field("Uncomfirmedtx", int(output)) \
        .time(datetime.utcnow(), WritePrecision.NS)

    write_api = client.write_api(write_options=SYNCHRONOUS)

    write_api.write(bucket, org, point)

while True:
    getblockcount()
    getdifficulty()
    getunconfirmedtx()
    time.sleep(20)


#!/usr/bin/env python3

import sys
import time
import speedtest
import requests

DB_URI = 'http://localhost:8086/write?db=speedtest'


def inject_metrics(db_uri, measurement, value, timestamp):
    """ Inject the speedtest metrics into influxdb """
    try:
        data = '{} value={} {}'.format(measurement, value, timestamp)
        requests.post(db_uri, data=data)
    except requests.exceptions.ConnectionError as error:
        sys.stderr.write('Error connecting to influxdb: {}\n'.format(error))
        sys.exit(2)


if __name__ == '__main__':
    servers = []
    # If you want to test against a specific server
    # servers = [1234]

    s = speedtest.Speedtest()
    s.get_servers(servers)
    s.get_best_server()
    s.download()
    s.upload()
    s.results.share()

    results_dict = s.results.dict()
    now = time.time()
    timestamp = int(now) * 10**9
    for key, value in results_dict.items():
        inject_metrics(DB_URI, key, value, timestamp)
    print('Injected latest values at {}'.format(time.ctime(now)))

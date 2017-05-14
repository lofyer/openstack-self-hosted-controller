#!/usr/bin/env python2
import sys
import etcd

try:
    client = etcd.Client(host='127.0.0.1', port=4001)
except Exception as e:
    print("Etcd client init error: {}").format(e)

try:
    lock = client.get_lock("/test/lock")
except Exception as e:
    print("Get lock error: {}").format(e)

sys.exit(0)

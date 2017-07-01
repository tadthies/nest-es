#!/usr/bin/env python

import nest
import json
import datetime
from dateutil.tz import tzlocal
from elasticsearch import Elasticsearch

client_id = ""
client_secret = ""
access_token_cache_file = "token.json"

indexname = "nest"
doc_type = "nest"
elastichost='localhost:9200'

nestinfo = {}

napi = nest.Nest(client_id=client_id, client_secret=client_secret, access_token_cache_file=access_token_cache_file)

es = Elasticsearch(elastichost)

now = datetime.datetime.now(tzlocal())

month = now.strftime("%m")
year = now.strftime("%Y")
index = indexname + "-" + year + "-" + month

for structure in napi.structures:
  nestinfo['structure'] = structure.name

  for device in structure.thermostats:
    id = datetime.datetime.now(tzlocal())
    nestinfo['timestamp'] = id
    nestinfo['name'] = device.name
    nestinfo['where'] = device.where
    nestinfo['mode'] = device.mode
    nestinfo['fan'] = device.fan
    nestinfo['temperature'] = device.temperature
    nestinfo['humidity'] = device.humidity
    nestinfo['target'] = device.target
    nestinfo['ecohigh'] = device.eco_temperature.high
    nestinfo['ecolow'] = device.eco_temperature.low
    nestinfo['emergency'] = device.is_using_emergency_heat
    nestinfo['online'] = device.online
    es.index(index=index, doc_type=doc_type, id=id, body=nestinfo)

#!/usr/bin/env python

import requests
import json
from pprint import pprint

data = None

def getCatalog(target):
  for catalog in getData()['access']['serviceCatalog']:
    if catalog['type'] == target:
      return catalog

def getTenantID():
  return getToken()['tenant']['id']

def getPublicURL(target):
  return getCatalog(target)['endpoints'][0]['publicURL']

def requestData():
  global data
  config = json.load(open('config.json'))
  data = requests.post(\
    config["token_endpoint"],\
    data=json.dumps({u"auth":config["auth"]}),\
    headers={'Content-Type':'application/json'}\
  )
  data = json.loads(data.text)

def getData():
  global data
  if data is None:
    requestData()
  return data

def getToken():
  return getData()['access']['token'] 

def getTokenID():
  return getToken()['id']

def makeRequest(method, target, endpoint, data=None):
  url = getPublicURL(target)
  endpoint = endpoint.replace("{tenant_id}", getTenantID())
  headers = {'X-Auth-Token':getTokenID()}
  if type(data) is dict:
    headers['Content-Type'] = 'application/json'
    data = json.dumps(data)
  print url+endpoint
  return requests.request(
    method,
    url+endpoint,
    headers=headers,
    data=data
  )

def pp(data):
  pprint(json.loads(data))


if __name__ == "__main__":
  print makeRequest('get','compute','/servers').text


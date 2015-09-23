import requests
import json

# GET
def get(url, params):
	return requests.get(url, params=params)

# POST with form-encoded data
def post(url, params):
	return requests.post(url, data=params)

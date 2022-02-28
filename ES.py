from elasticsearch import Elasticsearch

import json

es = Elasticsearch("http://localhost:9200", extra_headers={'Any': 'header'})
index_name = "malak_index_dev"
file = open("fichier.json")
json_array = json.load(file)

response = es.indices.create(index=index_name, ignore=400)
print("start injecting data")
for record in json_array:
    data = (record.items())
    for key, value in data:
        response = es.index(index=index_name, doc_type="json_data", body=value)
        print("insert : ", response['_id'], "----result : ", response['result'])
print("end injecting data")

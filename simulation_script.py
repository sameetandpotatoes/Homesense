from index import helper

groupId = "0083ef41-ed9c-43f1-99a4-6a714d73ecb7"
sensorId = "8ee163bc-9e7e-4d4e-a584-abfb78e71613"
payload = {}
payload["homeWindowOpen"] = "true"
payload["homeGarageOpen"] = "true"
url = "https://a6.cfapps.io/groups/"+groupId+"/sensors/"+sensorId+"/data"
print url
data = helper.post_request(url, payload)
print data

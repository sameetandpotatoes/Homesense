from index import helper
# Should close both
groupId = "b679a3c5-6349-4d86-b05e-e75338f2be86"
sensorId = "4777e5c2-4750-4e31-9308-411b4b7fb6d3"
payload = {}
payload["homeWindowOpen"] = "true"
payload["homeGarageOpen"] = "true"
url = "https://a6.cfapps.io/groups/"+groupId+"/sensors/"+sensorId+"/data"
data = helper.post_request(url, payload)
print data

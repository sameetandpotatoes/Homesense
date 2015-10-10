from index import helper

groupId = "b679a3c5-6349-4d86-b05e-e75338f2be86"
sensorId = "e14865d9-d942-4dd2-a10b-9e1c1bc1bec2"
payload = {}
payload["homeSmokeAlarmOn"] = "true"
url = "https://a6.cfapps.io/groups/"+groupId+"/sensors/"+sensorId+"/data"
print url
data = helper.post_request(url, payload)
print data

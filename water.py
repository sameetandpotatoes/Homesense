from index import helper

groupId = "b679a3c5-6349-4d86-b05e-e75338f2be86"
sensorId = "2f5facc7-2c13-4d87-9967-8b3b55052514"
payload = {}
payload["homeWaterSensorAlarmOn"] = "true"
url = "https://a6.cfapps.io/groups/"+groupId+"/sensors/"+sensorId+"/data"
print url
data = helper.post_request(url, payload)
print data

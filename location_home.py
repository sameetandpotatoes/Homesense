from index import helper

groupId = "b679a3c5-6349-4d86-b05e-e75338f2be86"
sensorId = "7e1862a3-1882-4c12-8791-1b46acd9ae13"
payload = {}
payload["tripSummaryUpload"] = "3"
payload["vehicleHealthUpload"] = "true"
url = "https://a6.cfapps.io/groups/"+groupId+"/sensors/"+sensorId+"/data"
print url
data = helper.post_request(url, payload)
print data

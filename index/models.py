from django.db import models

class Group(models.Model):
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=100)

class Sensor(models.Model):
    code = models.CharField(max_length=200, default = '')
    name = models.CharField(max_length=100)
    sensorType = models.CharField(max_length=200, default= '')
    zipCode = models.CharField(max_length=5, default = '')
    group = models.ForeignKey(Group, db_column='groupID')

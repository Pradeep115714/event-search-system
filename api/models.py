from django.db import models

class Event(models.Model):
    timestamp = models.DateTimeField()
    ip_address = models.CharField(max_length=50)
    action = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.timestamp} - {self.ip_address} - {self.action}"
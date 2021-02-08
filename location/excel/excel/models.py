from django.db import models
class person(models.Model):
    name = models.CharField(max_length= 50)
    email = models.EmailField(max_length= 50)
    location = models.CharField(max_length= 50, blank= True)



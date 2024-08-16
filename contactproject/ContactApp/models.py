from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ContactModel(models.Model):
    name=models.CharField(max_length=100)
    phone=models.IntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def _str_(self):
        return self.name
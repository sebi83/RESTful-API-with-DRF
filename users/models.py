from django.db import models


class UserModel(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, default="")
    username = models.CharField(max_length=100, default="")

    def __str__(self):
        return str(self.id)

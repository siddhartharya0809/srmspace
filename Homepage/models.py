from django.db import models
from django.db import connections
from django.contrib.auth.models import User


# Create your models here.
# class Signup(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     contact = models.CharField(max_length=10, null=True)
#     branch = models.CharField(max_length=40)
#     role = models.CharField(max_length=20)
#
#     def __str__(self):
#         return self.user.username


class Notes(models.Model):
    title = models.CharField(max_length=100, null=True)
    # upload_date = models.CharField(max_length=30)
    branch = models.CharField(max_length=40)
    semester = models.CharField(max_length=15, null=True)
    subject = models.CharField(max_length=20)
    file_type = models.FileField(upload_to='Notes/pdfs', null=True)
    description = models.CharField(max_length=400, null=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default="")
    email = models.CharField(max_length=100, default="")
    desc = models.CharField(max_length=1000, default="")

    def __str__(self):
        return self.name


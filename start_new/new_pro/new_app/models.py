from django.db import models


class student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email_id = models.EmailField(max_length=50)
    contact_no = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name

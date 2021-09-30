from django.db import models

# Create your models here.
class Job(models.Model):
    job_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)


    def __str__(self):
        return self.job_name
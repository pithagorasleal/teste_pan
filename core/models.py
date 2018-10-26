from django.db import models

# Create your models here.
class Step(models.Model):
    name = models.CharField(max_length=100, null=False)

class Process(models.Model):
    name = models.CharField(max_length=100, null=False)

class ProcessStepConfig(models.Model):
    step = models.ForeignKey(Step, on_delete=models.CASCADE)
    process = models.ForeignKey(Process, on_delete=models.CASCADE)
    time = models.IntegerField()
    order = models.IntegerField()
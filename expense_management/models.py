from django.db import models

# Create your models here.
class Expenses(models.Model):
    person = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    food = models.FloatField()
    rent = models.FloatField()
    loans = models.FloatField()
    utilities = models.FloatField()
    def __str__(self):
        return self.person

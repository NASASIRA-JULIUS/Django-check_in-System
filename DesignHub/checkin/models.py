from django.db import models

# Create your models here.

class visitor(models.Model):
    Name=models.CharField(max_length=40)
    Temperature=models.DecimalField(max_digits=10,decimal_places=2)
    Company=models.CharField(max_length=40)
    user_id=models.IntegerField(null=True, blank=True)
    Telephone=models.CharField(max_length=13)
    Date_created=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.Name

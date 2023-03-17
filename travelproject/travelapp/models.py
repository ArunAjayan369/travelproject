from django.db import models
# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='pics')
    discription=models.TextField()

class next(models.Model):
    Name = models.CharField(max_length=250)
    Image = models.ImageField(upload_to='pics')
    Discription = models.TextField()





    def __str__(self):
        return self.Name
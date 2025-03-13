from django.db import models

# Create your models here.
class Project(models.Model):
    Company = models.CharField(max_length=40)
    Project_name = models.CharField(max_length=50)
    year = models.CharField(max_length=4)  # Assuming year is a 4-digit number
    Project_photo = models.ImageField(upload_to='images')
    live_site_url = models.URLField()
    
    def __str__(self):
        return self.Project_name
    
class Description(models.Model):
    project = models.ForeignKey(Project, related_name='results', on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.description 
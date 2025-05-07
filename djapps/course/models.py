from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    
    class Meta:
        db_table = 'course'
        verbose_name = 'Course' 
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.name
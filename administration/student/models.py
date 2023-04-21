from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    physics_marks = models.IntegerField()
    chemistry_marks = models.IntegerField()
    maths_marks = models.IntegerField()
    computer_science_marks = models.IntegerField()

    def __str__(self) -> str:
        return self.name
    
    def total_marks(self):
        return self.physics_marks + self.chemistry_marks + self.maths_marks + self.computer_science_marks

    def percentage(self):
        return round((self.total_marks() / 400) * 100, 2)
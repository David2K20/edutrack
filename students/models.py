from django.db import models
from django.core.exceptions import ValidationError
import re

# Create your models here.

def nine_digit_validator(value):
    if len(str(value)) != 9:
        raise ValidationError(f'Enter a valid matric number.')
    
def name_validator(value):
    if not re.match(r'^[A-Za-z\s]+$', value):
        raise ValidationError('Name can only contain alphabetic characters and spaces.')

def field_study_validator(value):
    if not re.match(r'^[A-Za-z\s]+$', value):
        raise ValidationError('Field of study can only contain alphabetic characters and spaces.')


class Student(models.Model):
    matric_number = models.PositiveBigIntegerField(validators=[nine_digit_validator])
    first_name = models.CharField(max_length = 50, validators=[name_validator])
    last_name = models.CharField(max_length = 50, validators=[name_validator])
    email = models.EmailField(max_length = 100)
    field_of_study = models.CharField(max_length = 50, validators=[field_study_validator])
    cgpa = models.FloatField()
    photo = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f'Student: {self.first_name} {self.last_name}'
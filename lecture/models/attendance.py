
from .lecuture import Lecture
from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
User = get_user_model()
class YearInSchool(models.TextChoices):
    ATTENDANCE = 'attendance'
    ABSENCE = 'absence'
    LATE = 'late'
    
class Attendance(models.Model):
    attendance =  models.CharField(
        max_length=20,
        choices=YearInSchool.choices,
        default=YearInSchool.ATTENDANCE,
    )
    attendanceDate = models.DateTimeField()
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    
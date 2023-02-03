from django.db import models
from django.utils import timezone
from django.utils import datetime
from django.core.exceptions import ValidationError
# Create your models here.



def is_date_event(value):
        if value < timezone.now():
            raise ValidationError(
                ('%(value)s is not a valid date'),
                params={'value': value},
            )
        return value




class Event(models.Model):
    categorie_list=(
        ("Musique","Musique"),
        ("Sport","Sport"),
        ("Cinema","Cinema")
    )
    
    title = models.CharField(max_length=30)
    description=models.TextField()
    image=models.ImageField(null=True)
    categorie=models.CharField(choices=categorie_list,max_length=10)
    state=models.BooleanField(default=False)
    nbr_participant =models.IntegerField(default=0)
    evt_date=models.DateTimeField(null=True,validators=[is_date_event])
    created_date=models.DateField(auto_now_add=True)
    updated_date=models.DateField(auto_now=True)




class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(
                    date_evt__gte=datetime.now()
                ),
                name='Please check out the event date'
            ),
        ]










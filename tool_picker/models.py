from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.utils import timezone

class Tool(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=100, default='Uncategorized')
    case_management = models.BooleanField(default=False)
    fsp_integration = models.BooleanField(default=False)
    sms = models.BooleanField(default=False)
    biometrics = models.BooleanField(default=False)
    customized_workflows = models.BooleanField(default=False)
    setup_speed = models.IntegerField(default=0, validators=[
            MinValueValidator(0, message="Setup speed cannot be less than 0"),
            MaxValueValidator(4, message="Setup speed cannot be greater than 4"),
        ])
    setup_complexity = models.IntegerField(default=0, validators=[
            MinValueValidator(0, message="Setup complexity cannot be less than 0"),
            MaxValueValidator(4, message="Setup complexity cannot be greater than 4"),
        ])
    maintenance_complexity = models.IntegerField(default=0, validators=[
            MinValueValidator(0, message="Maintenance complexity cannot be less than 0"),
            MaxValueValidator(4, message="Maintenance complexity cannot be greater than 4"),
        ])
    training_and_support = models.IntegerField(default=0, validators=[
            MinValueValidator(0, message="Training and support cannot be less than 0"),
            MaxValueValidator(4, message="Training and support cannot be greater than 4"),
        ])
    transition = models.IntegerField(default=0, validators=[
            MinValueValidator(0, message="Transition cannot be less than 0"),
            MaxValueValidator(4, message="Transition cannot be greater than 4"),
        ])
    performance = models.IntegerField(default=0, validators=[
            MinValueValidator(0, message="Performance cannot be less than 0"),
            MaxValueValidator(4, message="Performance cannot be greater than 4"),
        ])
    connectivity = models.IntegerField(default=0, validators=[
            MinValueValidator(0, message="Connectivity cannot be less than 0"),
            MaxValueValidator(4, message="Connectivity cannot be greater than 4"),
        ])
    data_cleaning = models.IntegerField(default=0, validators=[
            MinValueValidator(0, message="Data cleaning cannot be less than 0"),
            MaxValueValidator(4, message="Data cleaning cannot be greater than 4"),
        ])
    data_viz = models.IntegerField(default=0, validators=[
            MinValueValidator(0, message="Data visualization cannot be less than 0"),
            MaxValueValidator(4, message="Data visualization cannot be greater than 4"),
        ])
    data_management_policies = models.IntegerField(default=0, validators=[
            MinValueValidator(0, message="Data management policies cannot be less than 0"),
            MaxValueValidator(4, message="Data management policies cannot be greater than 4"),
        ])
    interoperability = models.IntegerField(default=0, validators=[
            MinValueValidator(0, message="Interoperability cannot be less than 0"),
            MaxValueValidator(4, message="Interoperability cannot be greater than 4"),
        ])
    localization = models.IntegerField(default=0, validators=[
            MinValueValidator(0, message="Localization cannot be less than 0"),
            MaxValueValidator(4, message="Localization cannot be greater than 4"),
        ])
    data_security = models.IntegerField(default=0, validators=[
            MinValueValidator(0, message="Data security cannot be less than 0"),
            MaxValueValidator(4, message="Data security cannot be greater than 4"),
        ])
    date_added = models.DateTimeField(default=timezone.now)
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.name

class Testimonial(models.Model):
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
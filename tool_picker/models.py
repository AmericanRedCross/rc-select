from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.utils import timezone

class Tool(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=100, default='Uncategorized')
    case_management = models.BooleanField(default=False)
    case_management_desc = models.TextField(null=True)
    fsp_integration = models.BooleanField(default=False)
    fsp_integration_desc = models.TextField(null=True)
    sms = models.BooleanField(default=False)
    sms_desc = models.TextField(null=True)
    biometrics = models.BooleanField(default=False)
    biometrics_desc = models.TextField(null=True)
    customized_workflows = models.BooleanField(default=False)
    customized_workflows_desc = models.TextField(null=True)
    setup_speed = models.IntegerField(default=0, validators=[
            MinValueValidator(0, message="Setup speed cannot be less than 0"),
            MaxValueValidator(4, message="Setup speed cannot be greater than 4"),
        ])
    setup_speed_desc = models.TextField(default="No description provided.")
    setup_complexity = models.IntegerField(default=0, validators=[
            MinValueValidator(0, message="Setup complexity cannot be less than 0"),
            MaxValueValidator(4, message="Setup complexity cannot be greater than 4"),
        ])
    setup_complexity_desc = models.TextField(default="No description provided.")
    maintenance_complexity = models.IntegerField(default=0, validators=[
            MinValueValidator(0, message="Maintenance complexity cannot be less than 0"),
            MaxValueValidator(4, message="Maintenance complexity cannot be greater than 4"),
        ])
    maintenance_complexity_desc = models.TextField(default="No description provided.")
    training_and_support = models.IntegerField(default=0, validators=[
            MinValueValidator(0, message="Training and support cannot be less than 0"),
            MaxValueValidator(4, message="Training and support cannot be greater than 4"),
        ])
    training_and_support_desc = models.TextField(default="No description provided.")
    transition = models.IntegerField(default=0, validators=[
            MinValueValidator(0, message="Transition cannot be less than 0"),
            MaxValueValidator(4, message="Transition cannot be greater than 4"),
        ])
    transition_desc = models.TextField(default="No description provided.")
    performance = models.IntegerField(default=0, validators=[
            MinValueValidator(0, message="Performance cannot be less than 0"),
            MaxValueValidator(4, message="Performance cannot be greater than 4"),
        ])
    performance_desc = models.TextField(default="No description provided.")
    connectivity = models.IntegerField(default=0, validators=[
            MinValueValidator(0, message="Connectivity cannot be less than 0"),
            MaxValueValidator(4, message="Connectivity cannot be greater than 4"),
        ])
    connectivity_desc = models.TextField(default="No description provided.")
    data_cleaning = models.IntegerField(default=0, validators=[
            MinValueValidator(0, message="Data cleaning cannot be less than 0"),
            MaxValueValidator(4, message="Data cleaning cannot be greater than 4"),
        ])
    data_cleaning_desc = models.TextField(default="No description provided.")
    data_viz = models.IntegerField(default=0, validators=[
            MinValueValidator(0, message="Data visualization cannot be less than 0"),
            MaxValueValidator(4, message="Data visualization cannot be greater than 4"),
        ])
    data_viz_desc = models.TextField(default="No description provided.")
    data_management_policies = models.IntegerField(default=0, validators=[
            MinValueValidator(0, message="Data management policies cannot be less than 0"),
            MaxValueValidator(4, message="Data management policies cannot be greater than 4"),
        ])
    data_management_policies_desc = models.TextField(default="No description provided.")
    interoperability = models.IntegerField(default=0, validators=[
            MinValueValidator(0, message="Interoperability cannot be less than 0"),
            MaxValueValidator(4, message="Interoperability cannot be greater than 4"),
        ])
    interoperability_desc = models.TextField(default="No description provided.")
    localization = models.IntegerField(default=0, validators=[
            MinValueValidator(0, message="Localization cannot be less than 0"),
            MaxValueValidator(4, message="Localization cannot be greater than 4"),
        ])
    localization_desc = models.TextField(default="No description provided.")
    data_security = models.IntegerField(default=0, validators=[
            MinValueValidator(0, message="Data security cannot be less than 0"),
            MaxValueValidator(4, message="Data security cannot be greater than 4"),
        ])
    data_security_desc = models.TextField(default="No description provided.")
    date_added = models.DateTimeField(default=timezone.now)
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.name

class Testimonial(models.Model):
    # specify options for use_type field
    use_type_choices = (
        ('emergency-response', 'Emergency Response'),
        ('non-emergency', 'Project'),
    )
    
    use_type = models.CharField(max_length=50, choices=use_type_choices)
    related_emergency_name = models.CharField(max_length=200, default="No emergency specified.", null=True)
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
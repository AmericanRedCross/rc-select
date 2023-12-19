import datetime
import secrets

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.utils import timezone

class ToolAttributeDefinition(models.Model):
    default_def = "Not specified."
    
    # cost
    cost_def = models.TextField(default=default_def, null=True)
    cost1 = models.TextField(default=default_def, null=True)
    cost2 = models.TextField(default=default_def, null=True)
    cost3 = models.TextField(default=default_def, null=True)
    cost4 = models.TextField(default=default_def, null=True)
    
    # setup time
    setup_time_def = models.TextField(default=default_def, null=True)
    setup_time1 = models.TextField(default=default_def, null=True)
    setup_time2 = models.TextField(default=default_def, null=True)
    setup_time3 = models.TextField(default=default_def, null=True)
    setup_time4 = models.TextField(default=default_def, null=True)
    
    # setup complexity
    setup_complexity_def = models.TextField(default=default_def, null=True)
    setup_complexity1 = models.TextField(default=default_def, null=True)
    setup_complexity2 = models.TextField(default=default_def, null=True)
    setup_complexity3 = models.TextField(default=default_def, null=True)
    setup_complexity4 = models.TextField(default=default_def, null=True)
    
    # maintenance
    maintenance_def = models.TextField(default=default_def, null=True)
    maintenance1 = models.TextField(default=default_def, null=True)
    maintenance2 = models.TextField(default=default_def, null=True)
    maintenance3 = models.TextField(default=default_def, null=True)
    maintenance4 = models.TextField(default=default_def, null=True)
    
    # closeout
    closeout_def = models.TextField(default=default_def, null=True)
    closeout1 = models.TextField(default=default_def, null=True)
    closeout2 = models.TextField(default=default_def, null=True)
    closeout3 = models.TextField(default=default_def, null=True)
    closeout4 = models.TextField(default=default_def, null=True)
    
    # training and support resources
    support_def = models.TextField(default=default_def, null=True)
    support1 = models.TextField(default=default_def, null=True)
    support2 = models.TextField(default=default_def, null=True)
    support3 = models.TextField(default=default_def, null=True)
    support4 = models.TextField(default=default_def, null=True)
    
    # performance
    performance_def = models.TextField(default=default_def, null=True)
    performance1 = models.TextField(default=default_def, null=True)
    performance2 = models.TextField(default=default_def, null=True)
    performance3 = models.TextField(default=default_def, null=True)
    performance4 = models.TextField(default=default_def, null=True)
    
    # connectivity
    connectivity_def = models.TextField(default=default_def, null=True)
    connectivity1 = models.TextField(default=default_def, null=True)
    connectivity2 = models.TextField(default=default_def, null=True)
    connectivity3 = models.TextField(default=default_def, null=True)
    connectivity4 = models.TextField(default=default_def, null=True)
    
    # data cleaning
    data_cleaning_def = models.TextField(default=default_def, null=True)
    data_cleaning1 = models.TextField(default=default_def, null=True)
    data_cleaning2 = models.TextField(default=default_def, null=True)
    data_cleaning3 = models.TextField(default=default_def, null=True)
    data_cleaning4 = models.TextField(default=default_def, null=True)
    
    # data viz
    data_viz_def = models.TextField(default=default_def, null=True)
    data_viz1 = models.TextField(default=default_def, null=True)
    data_viz2 = models.TextField(default=default_def, null=True)
    data_viz3 = models.TextField(default=default_def, null=True)
    data_viz4 = models.TextField(default=default_def, null=True)
    
    # interoperability
    interoperability_def = models.TextField(default=default_def, null=True)
    interoperability1 = models.TextField(default=default_def, null=True)
    interoperability2 = models.TextField(default=default_def, null=True)
    interoperability3 = models.TextField(default=default_def, null=True)
    interoperability4 = models.TextField(default=default_def, null=True)
    
    # localization
    localization_def = models.TextField(default=default_def, null=True)
    localization1 = models.TextField(default=default_def, null=True)
    localization2 = models.TextField(default=default_def, null=True)
    localization3 = models.TextField(default=default_def, null=True)
    localization4 = models.TextField(default=default_def, null=True)
    
    # corresponding tech
    corresponding_tech_def = models.TextField(default=default_def, null=True)
    corresponding_tech1 = models.TextField(default=default_def, null=True)
    corresponding_tech2 = models.TextField(default=default_def, null=True)
    corresponding_tech3 = models.TextField(default=default_def, null=True)
    corresponding_tech4 = models.TextField(default=default_def, null=True)
    
    # data privacy
    data_privacy_def = models.TextField(default=default_def, null=True)
    data_privacy1 = models.TextField(default=default_def, null=True)
    data_privacy2 = models.TextField(default=default_def, null=True)
    data_privacy3 = models.TextField(default=default_def, null=True)
    data_privacy4 = models.TextField(default=default_def, null=True)
    
    # data protection
    data_protection_def = models.TextField(default=default_def, null=True)
    data_protection1 = models.TextField(default=default_def, null=True)
    data_protection2 = models.TextField(default=default_def, null=True)
    data_protection3 = models.TextField(default=default_def, null=True)
    data_protection4 = models.TextField(default=default_def, null=True)
    
    date_added = models.DateTimeField(default=timezone.now)
    date_modified = models.DateTimeField(auto_now=True)

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
    cost = models.IntegerField(default=0, validators=[
        MinValueValidator(0, message="Cost cannot be less than 0"),
        MaxValueValidator(4, message="Cost cannot be greater than 4"),
        ])
    cost_desc = models.TextField(default="No description provided.")
    date_added = models.DateTimeField(default=timezone.now)
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.name

class Testimonial(models.Model):
    # specify options for use_type field
    use_type_choices = (
        ("emergency-response", "Emergency Response"),
        ("non-emergency", "Project"),
    )
    
    use_type = models.CharField(max_length=50, choices=use_type_choices, default="Emergency Response")
    related_emergency_name = models.CharField(max_length=200, default="No emergency specified.", null=True)
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

class ToolPicker(models.Model):
    intended_use_type_choices = (
        ('emergency-response', 'Emergency Response'),
        ('non-emergency', 'Project'),
    )
    
    intended_use_type = models.CharField(max_length=50, choices=intended_use_type_choices)
    available_budget = models.IntegerField(default=1, validators=[
            MinValueValidator(1, message="Available budget cannot be less than 1"),
            MaxValueValidator(4, message="Available budget cannot be greater than 4"),
        ])
    setup_time = models.IntegerField(default=1, validators=[
            MinValueValidator(1, message="Setup time cannot be less than 1"),
            MaxValueValidator(4, message="Setup time cannot be greater than 4"),
        ])
    setup_complexity = models.IntegerField(default=1, validators=[
        MinValueValidator(1, message="Setup complexity cannot be less than 1"),
        MaxValueValidator(4, message="Setup complexity cannot be greater than 4"),
    ])
    
class ToolPickerResponses(models.Model):
    default_selection = "No data provided."
    
    unique_id = models.CharField(max_length=100, null=True, default="Not entered.")
    intended_use_type = models.CharField(max_length=50, default=default_selection)
    available_budget = models.IntegerField(default=0)
    setup_time = models.IntegerField(default=0)
    setup_complexity = models.IntegerField(default=0)
    
    def __repr__():
        f"{unique_id}-{intended_use_type}-budget={available_budget}"
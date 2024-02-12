from django.contrib import admin
from .models import Tool, ToolAttributeDefinition, ToolFeature

admin.site.register(Tool)
admin.site.register(ToolAttributeDefinition)
admin.site.register(ToolFeature)
admin.site.site_header = "RC Select Admin Portal"
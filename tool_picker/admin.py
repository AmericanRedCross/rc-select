from django.contrib import admin
from .models import Tool, ToolAttributeDefinition

admin.site.register(Tool)
admin.site.register(ToolAttributeDefinition)
admin.site.site_header = "RC Select Admin Portal"
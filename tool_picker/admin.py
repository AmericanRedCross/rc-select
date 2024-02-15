from django.contrib import admin
from .models import Tool, ToolAttributeDefinition, ToolFeature, ToolResource

admin.site.register(Tool)
admin.site.register(ToolAttributeDefinition)
admin.site.register(ToolFeature)
admin.site.register(ToolResource)
admin.site.site_header = "RC Select Admin Portal"
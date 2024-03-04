from django.contrib import admin
from django.utils.html import format_html
from .models import Tool, ToolAttributeDefinition, ToolFeature, ToolResource, Language

@admin.register(Tool)
class ToolAdmin(admin.ModelAdmin):
    """Create dynamic link to the tool image upload function on admin page"""
    readonly_fields = ('upload_tool_image_link',)  

    def upload_tool_image_link(self, obj):
        if obj.tool_image_url and obj.tool_image_url != 'none':
            url = "/upload_tool_image/{}/".format(obj.id) 
            return format_html(f'<a href="{url}" target="_blank">Click to upload a new tool icon.</a>')
        else:
            return "Can't upload image yet - save the tool first then return to this page."
    
    filter_horizontal = ('tool_resources','languages', 'tool_features')

# admin.site.register(Tool)
admin.site.register(ToolAttributeDefinition)
admin.site.register(ToolFeature)
admin.site.register(ToolResource)
admin.site.register(Language)
admin.site.site_header = "RC Select Admin Portal"
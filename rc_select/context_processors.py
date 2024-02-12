from datetime import datetime
from tool_picker.models import Tool

def global_data(request):
    # define list of tools for header dropdown menu
    tool_list = Tool.objects.all()
    
    return {
        'tool_list': tool_list,
        'now': datetime.now(),
    }
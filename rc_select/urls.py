from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from tool_picker import views as tool_picker_views

urlpatterns = [
    path('', tool_picker_views.home, name='index'),
    path('about/', tool_picker_views.about, name='tool-picker-about'),
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('get_cost_data/', tool_picker_views.get_cost_data, name='get_cost_data'),
    path('tool/', tool_picker_views.tool_info, name='tool-info'),
    path('tool_selection/', tool_picker_views.tool_selection_walkthrough, name='tool_selection_begin'),
    path('tool_picker_results/', tool_picker_views.tool_picker_results, name='tool_picker_results'),
]

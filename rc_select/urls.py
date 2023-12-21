from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from tool_picker import views as tool_picker_views

urlpatterns = [
    path('', tool_picker_views.home, name='index'),
    path('about/', tool_picker_views.about, name='tool-picker-about'),
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('get_closeout_data/', tool_picker_views.get_closeout_data, name='get_closeout_data'),
    path('get_connectivity_data/', tool_picker_views.get_connectivity_data, name='get_connectivity_data'),
    path('get_cost_data/', tool_picker_views.get_cost_data, name='get_cost_data'),
    path('get_data_cleaning_data/', tool_picker_views.get_data_cleaning_data, name='get_data_cleaning_data'),
    path('get_data_privacy_data/', tool_picker_views.get_data_privacy_data, name='get_data_privacy_data'),
    path('get_data_protection_data/', tool_picker_views.get_data_protection_data, name='get_data_protection_data'),
    path('get_data_viz_data/', tool_picker_views.get_data_viz_data, name='get_data_viz_data'),
    path('get_interoperability_data/', tool_picker_views.get_interoperability_data, name='get_interoperability_data'),
    path('get_localization_data/', tool_picker_views.get_localization_data, name='get_localization_data'),
    path('get_maintenance_data/', tool_picker_views.get_maintenance_data, name='get_maintenance_data'),
    path('get_performance_data/', tool_picker_views.get_performance_data, name='get_performance_data'),
    path('get_setup_time_data/', tool_picker_views.get_setup_time_data, name='get_setup_time_data'),
    path('get_setup_complexity_data/', tool_picker_views.get_setup_complexity_data, name='get_setup_complexity_data'),
    path('get_support_data/', tool_picker_views.get_support_data, name='get_support_data'),
    path('load_toolbox/', tool_picker_views.load_toolbox, name='load_toolbox'),
    path('tool/', tool_picker_views.tool_info, name='tool-info'),
    path('tool_selection/', tool_picker_views.tool_selection_walkthrough, name='tool_selection_begin'),
    path('tool_picker_results/', tool_picker_views.tool_picker_results, name='tool_picker_results'),
]

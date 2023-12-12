from django.contrib import admin
from django.urls import path, include

from tool_picker import views

urlpatterns = [
    path('tool_picker/', include("tool_picker.urls")),
    path('admin/', admin.site.urls),
]

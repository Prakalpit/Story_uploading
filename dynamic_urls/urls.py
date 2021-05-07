from django.contrib import admin
from django.urls import path, include

admin.site.site_header= "Stories Admin"
admin.site.site_title="Welcome to the admin"
admin.site.index_title="Story Admin"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('story.urls')),
]

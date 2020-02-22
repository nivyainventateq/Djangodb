from django.contrib import admin
from django.urls import path,include
from complaint.views import test

urlpatterns = [
    path('admin/', admin.site.urls),
    path('file/', view=test,name='test'),
]
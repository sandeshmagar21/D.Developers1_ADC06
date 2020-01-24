
from django.contrib import admin
from django.urls import path, include  
from gymapp.views import view_authenticate_users,view_register_users

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gymapp.urls'))

]



from django.urls import path
from .views import *
from gym.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static


urlpatterns = [

    # path('', home, name='home'),
    path('', index, name = 'index'),
    path('upload/', upload, name = 'sachin'),
    path('update/<int:gym_id>', update_form),
    path('delete/<int:gym_id>', delete_form),
    path('search/', search_function_hai, name="khadka"),
    path('register/', view_register_users , name="hacker"),
    path('login/',view_authenticate_users, name = "freddie"),
    path('logout/', logout, name = "logout"),
    path('contact', contact, name='contact'),
    path('home/', home, name='home'),
    path('course/', course, name='course'),
    path('access/', accesspage, name='access'),
    path('create/', trainer_create_form, name = "trainer"),
    path('abc/', abc_create_form, name='abc'),
    path('member/', members_create_form, name='members'),
    path('payment/', Payment_create_form, name='payment'),
    path('schedule/', schedulepage, name='schedule'),
    path('singuppage/', singuppage, name='singuppage'),
    path('tdm/', trainderdet, name="tdk"),
    path('accesspage/', view_accesspage_by_authorized_user, name='accesspage')
    
    
]




if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)
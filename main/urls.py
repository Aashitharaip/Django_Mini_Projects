from django.urls import path
from . import views

urlpatterns =[
    path('',views.index,name='index'),
    path('jokes',views.jokes,name='jokes'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('contactus',views.contactus,name='contactus'),
    path('pastebin',views.pastebin,name='pastebin'),
    path('pastebin/<str:code>',views.pastebin_output,name='pastebin_output'),
]

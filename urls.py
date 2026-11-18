from django.urls import path
from . import views

app_name='blog'
urlpatterns=[
    path("",views.index,name="index"),#root url defined by double quote
    path("post/<str:slug>/",views.detail,name="detail"),#<int:post_id>dynamically call parameter
    path("new_url1",views.new_url,name="new_url"),
    path("old_url_redirect",views.old_url_redirect,name="old_url_redirect"),
    path("contact",views.contact_view,name="contact"),
    path("about",views.about_view,name="about"),
        
    
    ]

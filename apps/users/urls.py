from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^register$', views.create_new_user),
  url(r'^login$', views.login),
  url(r'users/new$', views.create_new_user),
  url(r'^users$', views.display_users)
]
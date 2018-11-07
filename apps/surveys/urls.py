from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.display_surveys),
  url(r'new$', views.make_new_survey)
]
from django.conf.urls import url
from . import views
from django.contrib.auth.views import login
#'.' means look into project folders

urlpatterns = [
    url(r'^$', login,{'template_name':'accounts/login.html'}),
    url(r'accounts/',views.home)
]
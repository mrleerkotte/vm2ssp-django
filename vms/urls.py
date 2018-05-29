from django.urls import path, re_path

from . import views

urlpatterns = [
        re_path(r'^destroy/(?P<customer_id>\d+)/(?P<environment>\w+)', views.destroy_environment),
        re_path(r'^deploy/(?P<customer_id>\d+)/(?P<environment>\w+)', views.deploy_environment),
        path('', views.index, name='index'),
]

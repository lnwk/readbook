
from django.conf.urls import url
import views


urlpatterns=[
    url(r'^$', views.cart),
    url(r'^add(\d+)/$', views.add),

    url(r'^delete(\d+)/$', views.delete),

]
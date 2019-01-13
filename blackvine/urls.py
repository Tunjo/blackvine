from django.conf.urls import include, url
from django.contrib import admin
from shop.views import HomePage


urlpatterns = [

    url(r'^$', HomePage.as_view(), name="home"),
    url(r'^register/$', 'blackvine.users.views.customer_new', name='cus-new'),
    url(r'^admin/', include(admin.site.urls)),
]

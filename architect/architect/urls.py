from django.conf.urls import include, url
from django.contrib import admin
from userCenter.views.home_page import index, contact_us, login_views, register_views

urlpatterns = [
    # Examples:
    # url(r'^$', 'architect.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/', include('userCenter.urls')),
    url(r'^$', index, name='index'),
    # url(r'^login$', login_views, name='login'),
    # url(r'^register$', register_views, name='register'),
    url(r'^contact_us$', contact_us, name='contact_us')
]

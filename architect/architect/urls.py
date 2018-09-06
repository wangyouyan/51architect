from django.conf.urls import include, url
from django.contrib import admin
from official_website.views.home_page import index, contact_us

urlpatterns = [
    # Examples:
    # url(r'^$', 'architect.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/', include('userCenter.urls'), name='spare_parts'),
    url(r'^$', index, name='index'),
    url(r'^contact_us$', contact_us, name='contact_us')
]

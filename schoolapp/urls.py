from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'schoolapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^journal/', include('journal.urls')),
    url(r'^user/', include('user.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns(
    'django.contrib.auth.views',
    
    url(r'^login/$', 'login',
        {'template_name': 'login.html'},
        name='schoolapp_login'),
    
    url(r'^logout/$', 'logout',
        {'next_page': 'schoolapp_home'},
        name='schoolapp_logout'),  
)
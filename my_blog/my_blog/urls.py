from article.views import home, detail
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'my_blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),  #由于目前只有一个app, 方便起见, 就不设置include了
    url(r'^(?P<my_args>\d+)/$', detail, name='detail'),
]

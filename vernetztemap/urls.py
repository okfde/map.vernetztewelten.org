"""vernetztemap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
from django.views.decorators.cache import cache_page

from umap.urls import i18n_urls
from umap import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('', include('social_django.urls', namespace='social')),
    url(r'^m/(?P<pk>\d+)/$', views.MapShortUrl.as_view(),
        name='map_short_url'),
    url(r'^ajax-proxy/$', cache_page(180)(views.ajax_proxy),
        name='ajax-proxy'),
    url(r'^change-password/', auth_views.PasswordChangeView.as_view(),
        {'template_name': 'umap/password_change.html'},
        name='password_change'),
    url(r'^change-password-done/', auth_views.PasswordChangeDoneView.as_view(),
        {'template_name': 'umap/password_change_done.html'},
        name='password_change_done'),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^agnocomplete/', include('agnocomplete.urls')),
]

urlpatterns += i18n_patterns(
    url(r'^$', views.home, name="home"),
    url(r'^showcase/$', cache_page(24 * 60 * 60)(views.showcase),
        name='maps_showcase'),
    url(r'^search/$', views.search, name="search"),
    url(r'^about/$', views.about, name="about"),
    url(r'^user/(?P<username>[-_\w@]+)/$', views.user_maps, name='user_maps'),
    url(r'', include(i18n_urls)),
    prefix_default_language=False
)

if settings.DEBUG and settings.MEDIA_ROOT:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()

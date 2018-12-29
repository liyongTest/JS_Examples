"""static_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from learn import views as learn_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',learn_views.home,name='home'),
    url(r'^add/$',learn_views.index,name='add'),
    url(r'^fad/$',learn_views.fadeIn,name='fad'),
    url(r'^slide/$',learn_views.slide,name='slide'),
    url(r'^animate/$',learn_views.animate,name='animate'),
    url(r'^chaining/$',learn_views.chaining,name='chaining'),
    url(r'^jQueryHtml/$',learn_views.jquery_html,name='jQueryHtml'),
    url(r'^appendElement/$',learn_views.appendElement,name='appendElement'),
    url(r'^jqueryCSS/$',learn_views.jQueryCSS,name='jQueryCSS'),
    url(r'^ajax/$',learn_views.jQueryAjax,name='ajax'),
    url(r'php/$',learn_views.phpExample,name='php_examples'),
]

from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns( '',
        url(r'^$', views.index, name='index' ) ,
        url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'), # New!
        url(r'^add_category/$' , views.add_category, name='add_category' ), # NEW MAPPING!
        url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
        url(r'^register/$' , views.register, name='register' ) , # New!
        url(r'^login/$' , views.user_login, name='login' ) ,
        url(r'^xlm/' , views.xlm, name='xlm' ) ,
        url(r'^logout/$' , views.user_logout, name='logout' ) ,
)

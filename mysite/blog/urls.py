from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.shop_list, name = 'shop_list'),
    # url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    # url(r'^post/new/$', views.post_new, name = 'post_new'),
    # url(r'^post/(?P<pk>[0-9]+)/edit$', views.post_edit, name = 'post_edit'),
    # url(r'^drafts/$', views.post_draft_list, name = 'post_draft_list'),
    # url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name = 'post_publish'),
    # url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name = 'post_remove'),
    # url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name = 'add_comment_to_post'),
    # url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name = 'comment_remove'),
    # url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name = 'comment_approve'),
    url(r'^shop/new/$', views.shop_new, name = 'shop_new'),
    url(r'^shop/(?P<pk>\d+)/show/', views.shop_show, name = 'shop_show'),
    url(r'^shop/(?P<pk>\d+)/remove/$', views.shop_remove, name = 'shop_remove'),
    url(r'^shop/(?P<pk>\d+)/edit/$', views.shop_edit, name = 'shop_edit'),
    url(r'^visit/new$', views.visit_new, name = 'visit_new'),
    url(r'^visit/list$', views.visit_list, name = 'visit_list'),
    url(r'^visit/(?P<pk>\d+)/edit/$', views.visit_edit, name = 'visit_edit'),
    url(r'^visit/(?P<pk>\d+)/remove/$', views.visit_remove, name = 'visit_remove'),
]